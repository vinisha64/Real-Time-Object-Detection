import cv2
import torch

class YOLOv5Detector:
    def __init__(self):
        print("Loading YOLOv5 model...")

        self.model = torch.hub.load(
            'ultralytics/yolov5',
            'yolov5m',      # More accurate than yolov5s
            force_reload=False
        )

        # Detection confidence threshold
        self.model.conf = 0.25

        self.model.eval()

        self.cap = None

        print("YOLOv5 model loaded successfully!")

    def start_camera(self):
        self.cap = cv2.VideoCapture(0)

        # Set HD resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        if not self.cap.isOpened():
            raise RuntimeError("Cannot open webcam")

        return self.cap

    def detect(self, frame):
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.model(img_rgb)

        # Draw bounding boxes and labels
        results.render()

        detected_frame = cv2.cvtColor(
            results.ims[0],
            cv2.COLOR_RGB2BGR
        )

        return detected_frame

    def stop_camera(self):
        if self.cap:
            self.cap.release()
            self.cap = None