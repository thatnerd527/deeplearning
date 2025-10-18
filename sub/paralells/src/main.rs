use clap::Parser;
use csv::StringRecord;
use http::Request;
use image::{DynamicImage, ImageFormat, ImageReader, ImageResult};
use rayon::prelude::*;
use reqwest::blocking::{self, Client};
use serde::Serialize;
use std::{
    fs::{self, DirEntry, File, FileType},
    io::{Cursor, Read, Write},
    path::{self, Path, PathBuf},
    time::Duration,
};
use walkdir::WalkDir;
#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    #[arg(short, long)]
    inputfolder: PathBuf,
    #[arg(short, long)]
    outputfile: PathBuf,
}

#[derive(Clone, Debug)]
enum InputFile {
    Real { path: PathBuf, baseid: String },
    Csv { path: PathBuf, baseid: String },
}

#[derive(Debug, Serialize)]
struct CsvRecord {
    id: String,
    class_name: String,
    file_path: String,
    resolution: Option<String>,
}

#[derive(Debug, Serialize, Clone)]
struct Resolution {
    width: u32,
    height: u32,
}

#[derive(Clone, Debug)]
struct Batch {
    class_name: String,
    inputs: Vec<InputFile>,
    resolved_inputs: Vec<PathBuf>,
    converted: Vec<(PathBuf, Resolution)>,
}

use once_cell::sync::Lazy;
use regex::Regex;

fn is_allowed_format(x: &walkdir::DirEntry) -> bool {
    // Using `once_cell::sync::Lazy` ensures the regex is compiled only once,
    // the first time it's accessed, which is much more efficient than compiling
    // it on every function call.
    static IMAGE_REGEX: Lazy<Regex> =
        Lazy::new(|| Regex::new(r"(?i)\.(jpg|jpeg|png|gif|bmp|svg|webp)$").unwrap());

    // The regex explained:
    // (?i)   - Makes the match case-insensitive.
    // \.     - Matches the literal dot character.
    // (...)  - A capturing group for the extensions.
    // |      - Acts as an "OR" operator.
    // $      - Anchors the match to the end of the string.

    IMAGE_REGEX.is_match(x.file_name().to_str().unwrap())
        || x.file_name().to_str().unwrap().ends_with(".csv")
}

fn direntry_to_inputfile(x: walkdir::DirEntry) -> InputFile {
    let mut buf = Vec::new();
    let mut file = File::open(x.path()).unwrap();
    File::read_to_end(&mut file, &mut buf).unwrap();
    let digest = md5::compute(buf).0.to_vec();
    match x
        .file_name()
        .to_os_string()
        .into_string()
        .unwrap()
        .ends_with(".csv")
    {
        true => InputFile::Csv {
            path: x.into_path(),
            baseid: hex::encode(digest),
        },
        false => InputFile::Real {
            path: x.into_path(),
            baseid: hex::encode(digest),
        },
    }
}

fn process_batch(x: Batch) -> Batch {
    fn read_csv_and_download(csvfile: PathBuf, baseid: String) -> Vec<PathBuf> {
        let mut rdr = csv::Reader::from_reader(File::open(csvfile).unwrap());
        let collected = rdr.records().collect::<Vec<_>>();
        collected
        .into_par_iter()
        .map(
            |x| // The iterator yields Result<StringRecord, Error>, so we check the
            // error here.
            {
                let record = x.unwrap().get(0).unwrap().to_owned();
                let client = Client::builder()
                    .timeout(None)
                    .build()
                    .unwrap();
                let response = client.get(record)
                .send().unwrap().bytes().unwrap();
                let path = Path::new("steps/downloadtemp").join(baseid.clone() + "_");
                if !path.exists() {
                    fs::create_dir_all(path.clone().parent().unwrap()).unwrap();
                }
                let calculated = md5::compute(&response.to_vec()).0.to_vec();
                let created  =path.clone().to_str().unwrap().to_owned() + &hex::encode(calculated.clone()) + ".imgtemp";
                let mut resultfile = File::create(&created).unwrap();
                resultfile.write_all(&response.to_vec()).unwrap();
                Path::new(&created).to_path_buf()
            },
        )
        .collect::<Vec<_>>()
    }
    let mut dup = x.clone();
    dup.resolved_inputs = dup
        .inputs
        .iter()
        .filter_map(|x| match x {
            InputFile::Csv { path, baseid } => {
                Some(read_csv_and_download(path.clone(), baseid.clone()))
            }
            InputFile::Real { path, baseid } => Some(vec![path.clone()]),
        })
        .flatten()
        .collect::<Vec<_>>();
    dup
}

fn image_process(x: Batch) -> Batch {
    fn encode_image_to_bytes(image: DynamicImage, format: ImageFormat) -> ImageResult<Vec<u8>> {
        let mut buffer = Cursor::new(Vec::new());
        image.write_to(&mut buffer, format)?;
        Ok(buffer.into_inner())
    }
    let mut dup = x.clone();
    dup.converted = dup
        .resolved_inputs
        .clone()
        .into_par_iter()
        .filter_map(|x2| ImageReader::open(x2).ok())
        .filter_map(|x3| x3.with_guessed_format().ok())
        .filter_map(|x4| x4.decode().ok())
        .map(|x2| {
            let image = x2;
            let result = encode_image_to_bytes(image.clone(), ImageFormat::Png).unwrap();
            let hashed_name = hex::encode(md5::compute(&result).0.to_vec());
            let path = Path::new("steps/convertedtemp").join(hashed_name + ".png");
            if !path.exists() {
                fs::create_dir_all(path.clone().parent().unwrap()).unwrap();
            }
            let mut resultfile = File::create(&path).unwrap();
            resultfile.write_all(&result).unwrap();
            (
                Path::new(&path).to_path_buf(),
                Resolution {
                    width: image.width(),
                    height: image.height(),
                },
            )
        })
        .collect::<Vec<_>>();
    dup
}

fn main() {
    let args = Args::parse();
    if !args.inputfolder.exists() || args.inputfolder.is_file() {
        panic!("inputfolder has to be a folder, and has to exist")
    }
    let listed = fs::read_dir(args.inputfolder).unwrap();
    let preprocess = listed
        .map(|x| x.unwrap())
        .filter(|x| x.file_type().unwrap().is_dir())
        .map(|x| {
            let unwrapped = x;
            Batch {
                class_name: unwrapped.file_name().into_string().unwrap(),
                inputs: WalkDir::new(unwrapped.path())
                    .into_iter()
                    .filter_map(|x| x.ok())
                    .filter(|x| is_allowed_format(x))
                    .map(|x| direntry_to_inputfile(x))
                    .collect::<Vec<InputFile>>(),
                resolved_inputs: vec![],
                converted: vec![],
            }
        })
        .collect::<Vec<_>>();
    let processed = preprocess
        .into_par_iter()
        .map(|x| process_batch(x))
        .map(|x| image_process(x))
        .collect::<Vec<_>>();
    let mut wtr = csv::Writer::from_writer(File::create(args.outputfile).unwrap());
    for item in processed {
        item.converted.iter().for_each(|x| {
            wtr.serialize(CsvRecord {
                class_name: item.class_name.clone(),
                file_path: x.0.canonicalize().unwrap().to_str().unwrap().to_owned(),
                id: x.0.file_name().unwrap().to_str().unwrap().to_owned(),
                resolution: Some(format!("{}x{}", x.1.width, x.1.height)),
            })
            .unwrap();
        });
    }
    wtr.flush().unwrap();
}
