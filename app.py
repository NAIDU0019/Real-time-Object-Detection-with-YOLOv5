import streamlit as st
import torch
import cv2
import numpy as np

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

st.title("Real-time Object Detection with YOLOv5")

# Only webcam mode (no image upload)
st.subheader("Real-Time Webcam Detection")

# Button to start webcam
start = st.button("Start Webcam")

if start:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Could not open webcam.")
    else:
        stframe = st.empty()
        stop = False

        stop_btn = st.button("Stop Webcam", key="stop")  # Unique key to avoid duplication

        while cap.isOpened() and not stop:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to capture image from webcam.")
                break

            # YOLOv5 detection
            results = model(frame)
            results.render()
            frame_rgb = cv2.cvtColor(results.ims[0], cv2.COLOR_BGR2RGB)

            # Show in Streamlit
            stframe.image(frame_rgb, caption="Detected Objects", use_container_width=True)

            # Check if the stop button was pressed
            stop = st.session_state.get("stop_webcam", False)

        cap.release()
