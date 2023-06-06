from ultralytics import YOLO #Ultralytics is a mobile application that allows you to preview, export, and download your ML models created with Ultralytics HUB straight to your mobile device, and all in real-time! 

import cv2 #OpenCV has a function to read video, which is cv2. VideoCapture(). We can access our webcam using pass 0 in the function parameter. If you want to capture CCTV footage then we can pass RTSP url in the function parameter, which is really useful for video analysis

import cvzone #This is a Computer vision package that makes its easy to run Image processing and AI functions. At the core it uses OpenCV and Mediapipe libraries.

import math #math is a built-in module in the Python 3 standard library that provides standard mathematical constants and functions.
import time #the time() function returns the number of seconds passed since epoch (the point where time begins) 

# cap = cv2.VideoCapture(1)  # for video
# cap.set(3, 1280)
# cap.set(4, 720)




#----------------------------------------------------------------
import tkinter as tk
from tkinter import filedialog

# Create a tkinter window
root = tk.Tk()
root.withdraw() # Hide the root window

# Open a file dialog to select a video file
file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])

# Check if a file was selected
if file_path:
    # Open the video file
    cap = cv2.VideoCapture(file_path)
    # Pass the cap object to the code you provided and run it
    ...


model = YOLO("../Yolo-Weights/yolov5l.pt")

classNames = ["person", "bicycle", "car", "motorbike", "bus", "truck","traffic light", "stop sign","dog", "cow"]

prev_frame_time = 0
new_frame_time = 0

while True:
    new_frame_time = time.time()
    success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Class Name
            cls = int(box.cls[0])

            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

    fps = 1/ (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    print(fps)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
