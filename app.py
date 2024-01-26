import streamlit as st
import cv2
from PIL import Image
import numpy as np
from ultralytics import YOLO
import tempfile
import os
from datetime import datetime

model = YOLO("yolonas.pt")

def run_object_detection(image_or_video):
    results = model([image_or_video])[0]

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy.cpu().numpy().squeeze())
        conf, cls = float(box.conf), int(box.cls)

        if conf > 0:
            cv2.rectangle(image_or_video, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{results.names[cls]}: {conf:.2f}"
            cv2.putText(image_or_video, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return image_or_video

st.title("Object Detection App")
app_mode = st.selectbox("Choose the app mode", ["Image", "Video", "Webcam"])

if app_mode == "Image":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)  
    if st.button("Run Object Detection"):
        image = Image.open(uploaded_file)
        result_image = run_object_detection(np.array(image))
        st.image(result_image, caption="Object Detection Result", use_column_width=True)
        cv2.imwrite("OutputImages/"+datetime.now().strftime("%H-%M-%S")+".jpg",result_image)

elif app_mode == "Video":
    uploaded_file = st.file_uploader("Choose a video file...", type=["mp4", "avi"])

    if uploaded_file:
        st.video(uploaded_file, format="video/mp4")
        # output_path = st.text_input("Enter output video path", value="output.mp4")
        output_path = "OutputVideos/"+datetime.now().strftime("%H-%M-%S")+".webm"

        if st.button("Run Object Detection"):
            temp_path = tempfile.NamedTemporaryFile(delete=False)
            temp_path.write(uploaded_file.read())
            temp_path.close()

            cap = cv2.VideoCapture(temp_path.name)
            frame_width, frame_height = int(cap.get(3)), int(cap.get(4))
            fourcc = cv2.VideoWriter_fourcc(*"vp80")
            out = cv2.VideoWriter(output_path, fourcc, 30, (frame_width, frame_height), True)

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                frame = run_object_detection(frame)
                out.write(frame)

            cap.release()
            out.release()
            st.success("Video processing completed!")

            output_video_file = open(output_path, 'rb')
            st.video(output_video_file.read(), format="video/webm")

            os.remove(temp_path.name)

# Webcam detection
elif app_mode == "Webcam":
    live_stream = st.empty()
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = run_object_detection(frame)
        live_stream.image(frame, use_column_width=True)