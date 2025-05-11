import torch
import cv2

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # YOLOv5 expects RGB images, convert BGR to RGB
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Inference
    results = model(img_rgb)

    # Render results on frame
    rendered = results.render()[0]

    # Convert RGB back to BGR for OpenCV display
    output = cv2.cvtColor(rendered, cv2.COLOR_RGB2BGR)

    # Show the frame with detections
    cv2.imshow('YOLOv5 Real-Time Detection', output)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
