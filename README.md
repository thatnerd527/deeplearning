## Hello fellow lab assistants!

Welcome to the Deep Learning Lab Repository! This repository contains all the datasets and code necessary to complete the (IS794-AL) Deep Learning - LAB assignments.

## Folders

- **'datarealm'** : This folder contains the recent avocado dataset that is incorporated later after Midterm.
- **'scrapylab'** : This folder contains all the various image scrapers and web scrapers that we have used to collect data for our projects.
- **'steps/variations'** : This folder contains all the various variations / derivations of the datasets that have been created using `createDerivation.py`. This folder shouldn't be modified directly; instead, modify `createDerivation.py` to create new derivations.
- **'sub/paralells'** : This folder contains the Paralells sub-program for dataset prep, written in Rust. The purpose of this program is to speed up the dataset preparation process using multithreading; this program creates a fully prepared dataset from the raw images.

## Files

### Scripts & Configs
- **'createDerivation.py'** : This file is used to create new derivations of the dataset by applying various preprocessing techniques to the images.
- **'modeldef4.py'** : This python script contains the custom `DynamicResNetClassifier` class definition. It is imported by the modelling notebooks to allow for dynamic layer construction during hyperparameter tuning.
- **'yolo11x-seg.pt'** : This file contains the YOLOv11 segmentation model weights used for object-focused image segmentation in the preprocessing pipeline.
- **'requirements.txt'** : This file contains all the necessary python packages to run the code in this repository.
- **'DeepLearningRepo.code-workspace'** : This file is the VSCode workspace file for the repository.
- **'README.md'** : This file contains the information about the repository.

### Notebooks (Workflow Order)
1. **'Preprocessing v3.ipynb'** : The updated preprocessing pipeline. It integrates the Rust-based downloader and YOLOv11 segmentation to clean, crop, and prepare the dataset for modelling.
2. **'EDA.ipynb'** : Exploratory Data Analysis notebook used to inspect class distributions, visualize sample images, and verify the quality of the processed dataset.
3. **'Initial Modelling v2.ipynb'** : The **Baseline** modelling notebook. It trains the "All-in-one" and specialized models using manual tuning and no data augmentation to establish a performance baseline.
4. **'Final Modelling v2.ipynb'** : The **Optimized** modelling notebook. It implements the TPE (Tree-structured Parzen Estimator) algorithm via Optuna for automated hyperparameter tuning and includes the final rigorous evaluation metrics (F1-Score, Precision, Recall).

## Notes

This repo is designed to run within a podman container with NVIDIA Container Toolkit 1.17.8.

Download the container image from here: [Container Image Link](https://example.com/container-image)

Download NVIDIA Container Toolkit from here: [NVIDIA Container Toolkit Link](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.17.8/install-guide.html)

## Podman step instructions

1. Import the NvidiaAccel.tar image
2. Create the container using:
   ```bash
   podman run -it --name NvidiaAccel --security-opt=label=disable -v (your path):(your path) --device [nvidia.com/gpu=all](https://nvidia.com/gpu=all) docker.io/library/nvidiadl
3. Log into container:
    ```bash
    podman start NvidiaAccel ; podman exec -it NvidiaAccel
    ```
