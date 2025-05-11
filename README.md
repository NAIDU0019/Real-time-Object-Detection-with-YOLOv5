

# Real-time Object Detection with YOLOv5

This project implements real-time object detection using YOLOv5. The model is capable of detecting and classifying objects in real-time from webcam input. YOLOv5 is a state-of-the-art, real-time object detection model developed by Ultralytics, known for its speed and accuracy.

## 📸 Project Overview

The application uses YOLOv5 for detecting various objects in video streams. The model processes the webcam feed, identifies objects, and draws bounding boxes with class labels in real-time.
VISIT SITE:https://naidu0019-real-time-object-detection-with-yolov5-app-59pddp.streamlit.app/

## 🛠️ Features

* Real-time object detection using YOLOv5.
* Webcam integration for live video feed detection.
* Pre-trained YOLOv5 model weights for quick setup.
* Fast and efficient model with high accuracy.

## ⚙️ Setup Instructions

### Prerequisites

* Python 3.6+
* Git
* Webcam (for real-time object detection)

### Steps to Set Up

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/NAIDU0019/Real-time-Object-Detection-with-YOLOv5.git
   cd Real-time-Object-Detection-with-YOLOv5
   ```

2. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   Install the required libraries using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   Launch the object detection application:

   ```bash
   python app.py
   ```

   This will open a webcam feed and start detecting objects in real-time.

## 🧑‍💻 Code Overview

* **`app.py`**: Main script to run the object detection application.
* **`yolo_webcam.py`**: Integrates YOLOv5 with the webcam feed for real-time detection.
* **`requirements.txt`**: Python dependencies for the project.
* **`yolov5s.pt`**: Pre-trained YOLOv5 small model weights.

## 📊 Model

The model used in this project is YOLOv5, a fast and accurate object detection model. It detects objects and classifies them in a single pass, providing both bounding boxes and class labels.

For more information on YOLOv5, check out the official [Ultralytics YOLOv5 GitHub repository](https://github.com/ultralytics/yolov5).

## 📷 Example

Here is an example of the object detection in action:

![YOLOv5 Detection Example](path_to_example_image_or_video)

## 🚀 Contributing

Feel free to fork this repository, submit issues, or make pull requests. Contributions are welcome!

## 📝 License

This project is licensed under the MIT License.

---
