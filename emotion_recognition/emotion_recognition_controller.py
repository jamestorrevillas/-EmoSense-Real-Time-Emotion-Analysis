from datetime import datetime, timedelta

from PySide6.QtCore import QObject, QTimer, Signal, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt

from emotion_recognition.py_toggle.py_toggle import PyToggle
from emotion_recognition.emotion_recognition_engine import EmotionRecognitionEngine
from models.emotion_log import EmotionLog
from database.database import Database
import cv2

from session.user_session import UserSession


class EmotionRecognitionController(QObject):
    """
    Controller for the emotion recognition feature.

    This class manages the interaction between the UI, camera, and emotion recognition engine.
    It handles camera activation, frame processing, and emotion detection.

    Signals:
        emotion_detected (str, float): Emitted when an emotion is detected, with the emotion name and intensity.
        frame_processed (QImage): Emitted when a frame has been processed and is ready for display.
    """

    emotion_detected = Signal(str, float)
    frame_processed = Signal(QImage)

    def __init__(self, main_window):
        """
        Initialize the EmotionRecognitionController.

        Args:
            main_window: The main application window containing the emotion recognition page.
        """
        super().__init__()
        self.main_window = main_window
        self.emotion_recognition_page = main_window.emotion_recognition_page

        # Create custom toggle switches
        self._create_custom_toggles()

        # Connect UI elements
        self._connect_ui_elements()

        # Initialize emotion recognition components
        self.camera = None
        self.emotion_engine = EmotionRecognitionEngine()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.process_frame)

        # Connect signals
        self.frame_processed.connect(self.update_camera_feed)

        # Database
        self.db = Database()

        # Store the default pixmap
        self.default_pixmap = self.emotion_recognition_page.label_CameraFeed.pixmap()

        # Flag to track if camera sources have been populated
        self.camera_sources_populated = False

    def _create_custom_toggles(self):
        """Create custom toggle switches for activation and camera control."""
        old_checkbox_activate = self.emotion_recognition_page.checkBox_ToggleActivate
        self.custom_toggle_activate = PyToggle(old_checkbox_activate, width=60, height=30)
        old_checkbox_camera = self.emotion_recognition_page.checkBox_ToggleCameraOnOff
        self.custom_toggle_camera = PyToggle(old_checkbox_camera, width=60, height=30)

        # Update the references to the new toggles
        self.emotion_recognition_page.checkBox_ToggleActivate = self.custom_toggle_activate
        self.emotion_recognition_page.checkBox_ToggleCameraOnOff = self.custom_toggle_camera

    def _connect_ui_elements(self):
        """Connect UI elements to their respective slots."""
        self.custom_toggle_activate.stateChanged.connect(self.toggle_activation)
        self.custom_toggle_camera.stateChanged.connect(self.toggle_camera)
        self.emotion_recognition_page.comboBox_CameraSource.currentIndexChanged.connect(self.change_camera_source)

    def populate_camera_sources(self):
        """
        Populate the camera sources dropdown with available cameras.

        This method checks for up to 5 camera sources and adds them to the dropdown.
        It also sets the first detected camera as the current selection.
        """
        if self.camera_sources_populated:
            return

        self.emotion_recognition_page.comboBox_CameraSource.clear()

        camera_detected = False
        for index in range(5):  # Limit to 5 cameras to avoid excessive searching
            cap = cv2.VideoCapture(index)
            if cap.isOpened():
                self.emotion_recognition_page.comboBox_CameraSource.addItem(f"Camera {index}")
                cap.release()
                if not camera_detected:
                    camera_detected = True
                    self.emotion_recognition_page.comboBox_CameraSource.setCurrentIndex(0)

        if not camera_detected:
            self.emotion_recognition_page.label_ErrorMessageForCameraSettings.setText("No cameras detected")
        else:
            self.emotion_recognition_page.label_ErrorMessageForCameraSettings.clear()

        self.camera_sources_populated = True

    @Slot(int)
    def change_camera_source(self, index):
        """
        Change the current camera source.

        Args:
            index (int): The index of the selected camera source.
        """
        if self.custom_toggle_camera.isChecked():
            self.stop_camera()
            self.start_camera()
        self.emotion_recognition_page.label_ErrorMessageForCameraSettings.clear()

    def start_camera(self):
        """
        Start the camera with the currently selected source.

        If the camera fails to open, an error message is displayed.
        """
        camera_index = self.emotion_recognition_page.comboBox_CameraSource.currentIndex()
        self.camera = cv2.VideoCapture(camera_index)
        if self.camera.isOpened():
            self.timer.start(33)  # Process ~30 fps
        else:
            print(f"Failed to open camera {camera_index}")
            self.camera = None
            self.emotion_recognition_page.label_ErrorMessageForCameraSettings.setText(
                f"Failed to open camera {camera_index}")

    @Slot(int)
    def toggle_activation(self, state):
        """
        Toggle the activation of emotion recognition.

        Args:
            state (int): The state of the toggle (2 for checked, 0 for unchecked).
        """
        if state == 2:  # Checked
            if not self.custom_toggle_camera.isChecked():
                self.emotion_recognition_page.label_ErrorMessageForCameraSettings.setText(
                    "Please turn on the camera first")
                QTimer.singleShot(300, lambda: self.custom_toggle_activate.setChecked(False))  # Delay for animation
            else:
                self.start_emotion_recognition()

    @Slot(int)
    def toggle_camera(self, state):
        """
        Toggle the camera on or off.

        Args:
            state (int): The state of the toggle (2 for checked, 0 for unchecked).
        """
        if state == 2:  # Checked
            self.start_camera()
        else:  # Unchecked
            self.stop_camera()
            self.custom_toggle_activate.setChecked(False)

    def start_emotion_recognition(self):
        """
        Start the emotion recognition process.

        This method starts the timer for frame processing if the camera is open.
        If the camera is not open, it displays an error message.
        """
        if self.camera and self.camera.isOpened():
            self.timer.start(33)  # Process ~30 fps
        else:
            print("Camera is not open. Cannot start emotion recognition.")
            self.custom_toggle_activate.setChecked(False)
            self.emotion_recognition_page.label_ErrorMessageForCameraSettings.setText(
                "Camera is not open. Cannot start emotion recognition.")

    def stop_emotion_recognition(self):
        """Stop the emotion recognition process by stopping the timer."""
        self.timer.stop()

    def stop_camera(self):
        """
        Stop the camera and reset the UI.

        This method stops the timer, releases the camera, and resets the camera feed to the default pixmap.
        """
        self.timer.stop()
        if self.camera:
            self.camera.release()
            self.camera = None
        self.emotion_recognition_page.label_CameraFeed.setPixmap(self.default_pixmap)

    def process_frame(self):
        """
        Process a single frame from the camera.

        This method captures a frame from the camera, processes it for emotion recognition if activated,
        and emits the processed frame and detected emotions.
        """
        if self.camera and self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                frame = cv2.flip(frame, 1)  # Mirror the frame

                if self.custom_toggle_activate.isChecked():
                    processed_frame, emotions = self.emotion_engine.process_frame(frame)
                    if emotions:
                        self.save_emotion_log(emotions)
                        # Emit the emotion with the highest intensity
                        max_emotion = max(emotions, key=emotions.get)
                        self.emotion_detected.emit(max_emotion, emotions[max_emotion])
                else:
                    processed_frame = frame

                # Convert the frame to QImage for display
                rgb_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_frame.shape
                q_image = QImage(rgb_frame.data, w, h, ch * w, QImage.Format_RGB888)
                self.frame_processed.emit(q_image)
            else:
                self.stop_camera()
                self.custom_toggle_camera.setChecked(False)
                self.custom_toggle_activate.setChecked(False)
        else:
            self.stop_camera()
            self.custom_toggle_camera.setChecked(False)
            self.custom_toggle_activate.setChecked(False)

    @Slot(QImage)
    def update_camera_feed(self, q_image):
        """
        Update the camera feed display with the processed frame.

        Args:
            q_image (QImage): The processed frame as a QImage.
        """
        pixmap = QPixmap.fromImage(q_image)
        self.emotion_recognition_page.label_CameraFeed.setPixmap(pixmap)
        self.emotion_recognition_page.label_CameraFeed.setScaledContents(True)

    def save_emotion_log(self, emotions):
        """
        Save the detected emotions to the database.

        Args:
            emotions (dict): A dictionary of detected emotions and their intensities.
        """
        current_user = self.main_window.get_current_user()
        if current_user:
            log = EmotionLog(
                neutral=emotions['neutral'],
                happiness=emotions['happiness'],
                sadness=emotions['sadness'],
                anger=emotions['anger'],
                fear=emotions['fear'],
                surprise=emotions['surprise'],
                disgust=emotions['disgust'],
                contempt=emotions['contempt'],
                user_id=current_user.id
            )
            self.main_window.save_to_db(log)
        else:
            print("No user authenticated. Emotion log not saved.")

    def cleanup(self):
        """
        Perform cleanup operations when closing the emotion recognition page.

        This method stops all ongoing processes, releases resources, and resets the UI.
        """
        # Stop the timer if it's running
        if self.timer.isActive():
            self.timer.stop()

        # Release the camera if it's open
        if self.camera and self.camera.isOpened():
            self.camera.release()
            self.camera = None

        # Reset the camera feed to the default pixmap
        self.emotion_recognition_page.label_CameraFeed.setPixmap(self.default_pixmap)

        # Uncheck the toggle buttons
        self.custom_toggle_activate.setChecked(False)
        self.custom_toggle_camera.setChecked(False)

        # Clear any error messages
        self.emotion_recognition_page.label_ErrorMessageForCameraSettings.clear()

        # Reset the camera sources populated flag
        self.camera_sources_populated = False

        # Clear and reset the camera source combo box
        self.emotion_recognition_page.comboBox_CameraSource.clear()


if __name__ == "__main__":
    import sys
    from main import main

    sys.argv.append("emotion_recognition")
    main()