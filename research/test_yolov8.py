from ultralytics import YOLO
import cv2
# Load a model
model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model
img = cv2.imread('/home/ebi/Downloads/leo.jpg')
# Run batched inference on a list of images
results = model(img)  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs # Probs object for classification outputs
    x1, y1, x2, y2 = boxes.xyxy[0]
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

cv2.imshow('img', img)
cv2.waitKey(0)