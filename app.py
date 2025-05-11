import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import torch
import cv2

@st.cache_resource
def load_model():
    return torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)

model = load_model()

class YOLOv5Transformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        results = model(img)
        results.render()
        return results.ims[0]

st.title("🔍 Real-time Object Detection with YOLOv5")

webrtc_streamer(
    key="yolov5-stream",
    video_transformer_factory=YOLOv5Transformer,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)
