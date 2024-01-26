# Object Detection Project

This project utilizes Streamlit, OpenCV, and YOLO (You Only Look Once) for object detection in images, videos, and webcam streams.

## Setup Instructions

1. Install the required packages using pip:

```bash
pip install streamlit opencv-python-headless pillow numpy ultralytics
```

2. Clone this repository:

```bash
git clone <repository_url>
```

3. Navigate to the project directory:

```bash
cd <project_directory>
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

## Usage

1. Upon running the Streamlit app, you will see a dropdown menu to choose the app mode: "Image," "Video," or "Webcam."

2. If you select "Image":
   - Click on "Choose an image..." to upload an image file (supported formats: jpg, png, jpeg).
   - Click on "Run Object Detection" to detect objects in the uploaded image.
   - The resulting image with bounding boxes and labels will be displayed along with the timestamped output saved in the "OutputImages" directory.

3. If you select "Video":
   - Click on "Choose a video file..." to upload a video file (supported formats: mp4, avi).
   - Click on "Run Object Detection" to detect objects in the uploaded video.
   - The resulting video with bounding boxes and labels will be displayed along with the timestamped output saved in the "OutputVideos" directory.

4. If you select "Webcam":
   - The webcam feed will be displayed with real-time object detection.

## Libraries Used

- [Streamlit](https://streamlit.io/)
- [OpenCV](https://opencv.org/)
- [Pillow](https://python-pillow.org/)
- [NumPy](https://numpy.org/)
- [Ultralytics YOLO](https://github.com/ultralytics/yolov5)
