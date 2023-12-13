from torch import nn
import cv2
import math
from ultralytics import YOLO
import imutils

class Prediction():
    def __init__(self, model: nn.Module):
        self.model = YOLO(model)
        self.classNames = ["Brush"]
        
    def resize_frame(self, frame):
        resized_img = cv2.resize(frame, (416, 416))
        
        
        return resized_img
    def resize_bbox(self,frame,  x1, y1, x2, y2):
        
        x_scale = 416 / frame.shape[1]
        y_scale = 416 / frame.shape[0]
        
        x1 = int(x1 * x_scale)
        y1 = int(y1 * y_scale)
        x2 = int(x2 * x_scale)
        y2 = int(y2 * y_scale)
        
        return x1, y1, x2, y2
    
    
    def image(self, image):
        results = self.model(image, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                x1, y1, x2, y2 = self.resize_bbox(image, x1, y1, x2, y2)
                cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 255), 2)
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                cv2.putText(image, f"{self.classNames[cls]}", (max(0, x1), max(35, y1)), cv2.FONT_HERSHEY_COMPLEX, 2, 255)

        image = self.resize_frame(image)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def video(self, cap):
        cap.set(3, 416)
        cap.set(4, 416)
        while True:
            success, img = cap.read()
            results = self.model(img, stream=True)
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    # Bounding Box
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
                    # w, h = x2 - x1, y2 - y1
                    # cvzone.cornerRect(img, (x1, y1, w, h))
                    # Confidence
                    conf = math.ceil((box.conf[0] * 100)) / 100
                    # Class Name
                    cls = int(box.cls[0])
                    # print(cls)

                    # cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
                    # cv2.putText(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1) #cause AttributeError: 'NoneType' object has no attribute 'is_scripting'
                    cv2.putText(img, f"{self.classNames[cls]}", (max(0, x1), max(35, y1)), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)


            cv2.imshow("Image", img)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        cv2.destroyAllWindows()
        
    def webcame(self, cap):
        cap.set(3, 416)
        cap.set(4, 416)
        while True:
            success, img = cap.read()
            results = self.model(img, stream=True)
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    # Bounding Box
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
                    # w, h = x2 - x1, y2 - y1
                    # cvzone.cornerRect(img, (x1, y1, w, h))
                    # Confidence
                    conf = math.ceil((box.conf[0] * 100)) / 100
                    # Class Name
                    cls = int(box.cls[0])
                    # print(cls)

                    # cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
                    # cv2.putText(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1) #cause AttributeError: 'NoneType' object has no attribute 'is_scripting'
                    cv2.putText(img, f"{self.classNames[cls]}", (max(0, x1), max(35, y1)), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)


            cv2.imshow("Image", img)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        cv2.destroyAllWindows()