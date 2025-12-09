import time
from fastapi import FastAPI, File, UploadFile, Form, WebSocket, WebSocketDisconnect
from typing import Annotated
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from modeldef import load_model
import cv2
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

def extract_image_features_from_cv2(img_array: cv2.typing.MatLike) -> list[float]:
    img_resized = cv2.resize(img_array, (224, 224))
    img_array_expanded = np.expand_dims(img_resized, axis=0)
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

def classify_image_with_confidences(features: list[float]) -> tuple[str, dict[str, float]]:
    features_array = np.array(features).reshape(1, -1)
    predictions = classifierModel(torch.tensor(features_array, dtype=torch.float32))
    probabilities = torch.softmax(predictions, dim=1).detach().numpy()[0]
    predicted_class_idx = torch.argmax(predictions, dim=1).item()
    idx_to_class = {v: k for k, v in basejson["class_to_idx"].items()}
    predicted_class_label = idx_to_class[predicted_class_idx]
    
    class_confidences = {
        idx_to_class[i]: float(probabilities[i]) for i in range(len(probabilities))
    }
    
    return predicted_class_label, class_confidences

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

@app.post("/oneshot_image_confidences")
async def upload_form_with_confidences(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
    description: Annotated[str, Form()] = "No description provided"
):
    features = extract_image_features(file)
    predicted_class, confidences = classify_image_with_confidences(features)
    return {
        "predicted_class": predicted_class,
        "confidences": confidences,
        "description": description
    }

@app.websocket("/ws/socketprocessing")
async def video_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # 1. Receive the binary frame data
            data = await websocket.receive_bytes()
            start_time = time.perf_counter()
            # 2. Convert bytes to numpy array (decoding the image)
            # This is efficient; it doesn't write to disk
            nparr = np.frombuffer(data, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            if frame is None:
                continue
            features = extract_image_features_from_cv2(frame)
            predicted_class, confidences = classify_image_with_confidences(features)

            # --- YOUR PROCESSING LOGIC HERE ---
            # Example: Grayscale conversion or AI inference
            # processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Example: Print frame dimensions to prove it's working
            height, width, _ = frame.shape
            imageId = f"frame_{np.random.randint(1000,9999)}"
            end_time = time.perf_counter()
            latency_ms = (end_time - start_time) * 1000
            await websocket.send_json({
                "type": "detection",
                "predicted_class": predicted_class,
                "confidences": confidences,
                "imageId": imageId,
                "latencyMS": latency_ms
            })

    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Run this file directly to start the server
    uvicorn.run(app, host="0.0.0.0", port=2000)