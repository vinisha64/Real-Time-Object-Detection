import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
from object_detection_backend import YOLOv5Detector

class ObjectDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YOLOv5x Real-Time Detection")
        self.root.geometry("900x700")
        self.root.configure(bg="#E6E6FA")

        self.detector = YOLOv5Detector()
        self.cap = None
        self.running = False

        self.title = tk.Label(root, text="YOLOv5x Real-Time Object Detection", font=("Helvetica", 20, "bold"), bg="#FFFF00", fg="#333")
        self.title.pack(pady=10)

        self.canvas = tk.Label(root)
        self.canvas.pack()

        self.start_btn = tk.Button(root, text="Start Detection", font=("Helvetica", 14), bg="#4caf50", fg="Black", command=self.start_detection)
        self.start_btn.pack(pady=10)

        self.stop_btn = tk.Button(root, text="Stop Detection", font=("Helvetica", 14), bg="#f44336", fg="Black", command=self.stop_detection, state=tk.DISABLED)
        self.stop_btn.pack(pady=5)

    def start_detection(self):
        try:
            self.cap = self.detector.start_camera()
        except RuntimeError as e:
            messagebox.showerror("Error", str(e))
            return

        self.running = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.detect_loop()

    def stop_detection(self):
        self.running = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.detector.stop_camera()
        self.canvas.configure(image='')

    def detect_loop(self):
        if not self.running:
            return

        ret, frame = self.cap.read()
        if not ret:
            self.stop_detection()
            return

        detected = self.detector.detect(frame)
        img = Image.fromarray(cv2.cvtColor(detected, cv2.COLOR_BGR2RGB))
        imgtk = ImageTk.PhotoImage(image=img)
        self.canvas.imgtk = imgtk
        self.canvas.configure(image=imgtk)

        self.root.after(30, self.detect_loop)

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ObjectDetectionApp(root)
    root.mainloop()