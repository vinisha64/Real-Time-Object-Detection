import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import sys

class WelcomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome - Object Detection System")
        self.root.geometry("600x400")
        self.root.configure(bg="#ff1493")

        self.title = tk.Label(
            root,
            text="Welcome to Object Detection",
            font=("Helvetica", 22, "bold"),
            bg="#e0f7fa",
            fg="#000000"
        )
        self.title.pack(pady=30)

        self.image_btn = tk.Button(
            root,
            text="Image Detection",
            font=("Helvetica", 16),
            width=20,
            bg="#29b6f6",
            fg="white",
            command=self.image_detection
        )
        self.image_btn.pack(pady=15)

        self.video_btn = tk.Button(
            root,
            text="Video Detection",
            font=("Helvetica", 16),
            width=20,
            bg="#00796b",
            fg="white",
            command=self.video_detection
        )
        self.video_btn.pack(pady=15)

    def image_detection(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
        )

        if not file_path:
            return

        try:
            import torch
            import cv2
            from PIL import Image, ImageTk

            print("Loading YOLO model...")

            model = torch.hub.load(
                'ultralytics/yolov5',
                'yolov5s',
                force_reload=False
            )

            print("YOLO loaded successfully")

            img = cv2.imread(file_path)

            if img is None:
                raise Exception(f"Could not read image:\n{file_path}")

            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            results = model(img_rgb)

            detections = results.xyxy[0]

            for *box, conf, cls in detections:
                x1, y1, x2, y2 = map(int, box)

                label = f"{results.names[int(cls)]} {conf:.2f}"

                cv2.rectangle(
                    img_rgb,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    img_rgb,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

            pil_img = Image.fromarray(img_rgb)
            imgtk = ImageTk.PhotoImage(image=pil_img)

            popup = tk.Toplevel(self.root)
            popup.title("Detection Result")

            lbl = tk.Label(popup, image=imgtk)
            lbl.image = imgtk
            lbl.pack()

        except Exception as e:
            import traceback

            print("\n===== FULL ERROR =====")
            print(traceback.format_exc())
            print("======================\n")

            messagebox.showerror(
                "Error",
                f"Image detection failed:\n{str(e)}"
            )

    def video_detection(self):
        try:
            script_path = os.path.join(
                os.getcwd(),
                "object_detection_gui.py"
            )

            subprocess.Popen(
                [sys.executable, script_path]
            )

        except Exception as e:
            import traceback

            print("\n===== FULL ERROR =====")
            print(traceback.format_exc())
            print("======================\n")

            messagebox.showerror(
                "Error",
                f"Failed to start video detection.\n{str(e)}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeScreen(root)
    root.mainloop()