# Real-Time Object Detection System

This project aims to develop a real-time object detection system using the YOLO (You Only Look Once) model. The system is built using Python and utilizes various libraries such as Ultralytics, OpenCV, cvzone, math, and tkinter.

## Features
- Real-time object detection: The system can detect objects in real-time from video sources, such as webcams or pre-recorded video files.
- Easy video input: It supports accessing video streams from webcams or video files, providing flexibility in data sources.
- Bounding box visualization: Detected objects are highlighted with bounding boxes, making it easier to visualize their locations within the frames.
- Class labels and confidence scores: The system labels each detected object with its class name and corresponding confidence score, providing additional information about the objects.
- Frames per second (FPS) calculation: It calculates and displays the FPS value, giving an indication of the processing speed and system performance.

## Getting Started
1. Install the required libraries mentioned in the `requirements.txt` file.
2. Run the Python script `main.py`.
3. The script will open a file dialog to select a video file or use the webcam as the video source.
4. The real-time object detection system will process each frame, display bounding boxes and labels, and show the FPS value.

Feel free to customize the code based on your requirements and explore the functionalities provided by the Ultralytics, OpenCV, and cvzone libraries.

## Dependencies
- Ultralytics: Mobile application for ML model deployment
- OpenCV: Library for video processing and webcam access
- cvzone: Computer vision package for image processing and AI functions
- math: Python standard library for mathematical operations
- tkinter: GUI toolkit for creating the file dialog window

## Credits
- Ultralytics: [https://www.ultralytics.com](https://www.ultralytics.com)
- OpenCV: [https://opencv.org](https://opencv.org)
- cvzone: [https://github.com/codewithharry/cvzone](https://github.com/codewithharry/cvzone)

## License
This project is licensed under the [MIT License](LICENSE).
