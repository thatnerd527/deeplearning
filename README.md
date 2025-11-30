## Hello fellow lab assistants!

Welcome to the Deep Learning Lab Repository!, This repository contains all the datasets, and code necessary to complete the (IS794-AL) Deep Learning - LAB assignments.

## Folders

- 'datarealm' : This folder contains the recent avocado dataset that is incorporated later after Midterm.
- 'scrapylab' : this folder contains all the various image scrapers and web scrapers that we have used to collect data for our projects.
- 'steps/variations': 'This folder contains all the various veriations / derivations of the datasets that have been created using createDerivation.py, this folder shouldnt modified directly, instead modify createDerivation.py to create new derivations.'
- 'sub/paralells' : This folder contains the Paralells sub program for dataset prep, written in rust. The purpose of this program is to speed up the dataset preparation process using multithreading, this program created a fully prepared dataset from the raw images.

## Files

- 'createDerivation.py' : This file is used to create new derivations of the dataset, by applying various preprocessing techniques to the images.
- 'Preprocessing v2.ipynb' : This file contains the main preprocessing pipeline and EDA for the dataset, it uses createDerivation.py to create new derivations of the dataset.
- 'Feature Extraction.ipynb' : This file contains the feature extraction pipeline for the dataset, it uses ResNet50 to extract features from the images.
- 'Modelling.ipynb' : This file contains the modelling pipeline for the dataset, it uses a scratch built CNN model to classify the images.
- 'README.md' : This file contains the information about the repository.
- 'requirements.txt' : This file contains all the necessary python packages to run the code in this repository.
- 'DeepLearningRepo.code-workspace' : This file is the VSCode workspace file for the repository.
- 'yolo11x-seg.pt' : This file contains the YOLOv11 segmentation model weights used for image segmentation in the preprocessing pipeline.

## Notes

Feature Extraction and Modelling notebooks are still in progress and will be updated soon.

This repo is designed to with a podman container with NVIDIA Container Toolkit 1.17.8, download the container image from here: [Container Image Link](https://example.com/container-image)

Download NVIDIA Container Toolkit from here: [NVIDIA Container Toolkit Link](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.17.8/install-guide.html)

## Podman step instructions

1. Import the NvidiaAccel.tar image
2. Create the container using podman run -it --name NvidiaAccel --security-opt=label=disable -v (your path):(your path) --device nvidia.com/gpu=all docker.io/library/nvidiadl bash

Log into container: podman start NvidiaAccel ; podman exec -it NvidiaAccel bash
