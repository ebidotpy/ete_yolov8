from fastapi import APIRouter, File, UploadFile, Request
from App.utils.pred import Prediction
import numpy as np
import cv2
from fastapi.responses import HTMLResponse, StreamingResponse
from App.utils.single_camera import Camera




router = APIRouter(
    prefix="/pred", 
    tags=["pred"]
)


model = "/home/ebi/machinelearning/end_to_end_ml_projects/ete_yolov8/artifacts/yolov8/train/weights/best.pt"

@router.post("/image")
async def detect_objects(file: UploadFile):
    # process the uploaded image for object detection
    image_bytes = await file.read()
    image = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    detect = Prediction(model=model)
    detect.image(image=image)


@router.get("/video_feed")
async def video_feed():
    cap = cv2.VideoCapture(0)
    detect = Prediction(model=model)
    detect.webcame(cap=cap)



