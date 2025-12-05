from fastapi import FastAPI, File, UploadFile, Form
from typing import Annotated
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from modeldef import load_model
import numpy as np
import tempfile
import uvicorn
import json
import torch

app = FastAPI()

basejson: dict[str, any] = json.load(open("model_metadata.json"))

feModel = ResNet50(weights='imagenet', include_top=False, pooling='avg')
classifierModel = load_model(basejson["model_full_path"], basejson["num_features"], basejson["num_classes"])

def extract_image_features(file: UploadFile) -> list[float]:
    # create a temporary file to read the image
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        temp.write(file.file.read())
        temp.flush()
    
        img = image.load_img(temp.name, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array_expanded = np.expand_dims(img_array, axis=0)
        img_preprocessed = preprocess_input(img_array_expanded)
    

    features = feModel.predict(img_preprocessed)
    return features[0].tolist()

def classify_image(features: list[float]) -> str:
    features_array = np.array(features).reshape(1, -1)
    predictions = classifierModel(torch.tensor(features_array, dtype=torch.float32))
    predicted_class_idx = torch.argmax(predictions, dim=1).item()
    idx_to_class = {v: k for k, v in basejson["class_to_idx"].items()}
    predicted_class_label = idx_to_class[predicted_class_idx]
    return predicted_class_label

@app.post("/get_image_class")
async def upload_form(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
    description: Annotated[str, Form()] = "No description provided"
):
    features = extract_image_features(file)
    predicted_class = classify_image(features)
    return {
        "predicted_class": predicted_class,
        "description": description
    }

if __name__ == "__main__":
    # Run this file directly to start the server
    uvicorn.run(app, host="0.0.0.0", port=8000)