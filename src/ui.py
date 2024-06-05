import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2

class EmoSenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EmoSense")
        self.create_widgets()
        self.cap = None
        self.camera_index = 0
        self.camera_resolutions = [
            (640, 480),
            (800, 600),
            (1280, 720),
            (1920, 1080)
        ]
        self.current_resolution = self.camera_resolutions[0]

    def create_widgets(self):
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Real-Time Emotion Recognition Label
        ttk.Label(main_frame, text="Real-Time Emotion Recognition", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Activate/Deactivate buttons
        self.activate_button = ttk.Button(main_frame, text="Activate", command=self.activate_recognition)
        self.activate_button.grid(row=1, column=0, padx=5, pady=5)

        self.deactivate_button = ttk.Button(main_frame, text="Deactivate", command=self.deactivate_recognition)
        self.deactivate_button.grid(row=1, column=1, padx=5, pady=5)

        # Settings options
        ttk.Label(main_frame, text="Change Settings/Options", font=("Helvetica", 14)).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(main_frame, text="Turn camera on/off", command=self.toggle_camera).grid(row=3, column=0, padx=5, pady=5)
        ttk.Button(main_frame, text="Change camera resolution", command=self.change_resolution).grid(row=3, column=1, padx=5, pady=5)
        ttk.Button(main_frame, text="Select camera", command=self.select_camera).grid(row=4, column=0, columnspan=2, pady=5)

        # Placeholder for camera feed
        self.camera_feed = tk.Label(main_frame, text="Camera feed will appear here", background="grey", width=640, height=480)
        self.camera_feed.grid(row=5, column=0, columnspan=2, pady=10)

    def activate_recognition(self):
        messagebox.showinfo("Info", "Emotion recognition activated.")
        self.start_camera()

    def deactivate_recognition(self):
        messagebox.showinfo("Info", "Emotion recognition deactivated.")
        self.stop_camera()

    def toggle_camera(self):
        if self.cap is not None and self.cap.isOpened():
            self.stop_camera()
        else:
            self.start_camera()

    def change_resolution(self):
        current_index = self.camera_resolutions.index(self.current_resolution)
        next_index = (current_index + 1) % len(self.camera_resolutions)
        self.current_resolution = self.camera_resolutions[next_index]
        if self.cap is not None and self.cap.isOpened():
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.current_resolution[0])
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.current_resolution[1])
        messagebox.showinfo("Info", f"Resolution changed to {self.current_resolution[0]}x{self.current_resolution[1]}")

    def select_camera(self):
        self.camera_index = (self.camera_index + 1) % 2  # Assume you have two cameras for now
        if self.cap is not None and self.cap.isOpened():
            self.stop_camera()
            self.start_camera()
        messagebox.showinfo("Info", f"Camera changed to {self.camera_index}")

    def start_camera(self):
        self.cap = cv2.VideoCapture(self.camera_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.current_resolution[0])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.current_resolution[1])
        self.update_camera_feed()

    def stop_camera(self):
        if self.cap:
            self.cap.release()
            self.cap = None
        self.camera_feed.config(image='')

    def update_camera_feed(self):
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.camera_feed.imgtk = imgtk
                self.camera_feed.config(image=imgtk)
            self.root.after(10, self.update_camera_feed)

def start_app():
    root = tk.Tk()
    app = EmoSenseApp(root)
    root.mainloop()

if __name__ == "__main__":
    start_app()
