import sys

import cv2
import numpy as np
import tensorflow as tf
import mediapipe as mp
import os
import warnings

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.get_logger().setLevel('ERROR')

# Suppress MediaPipe warnings
warnings.filterwarnings("ignore", category=UserWarning, module="mediapipe")


class EmotionRecognitionEngine:
    """
    A class for performing emotion recognition on facial images.

    This class uses a TensorFlow Lite model to predict emotions from facial images,
    and MediaPipe for face detection and mesh drawing.
    """

    def __init__(self):
        """
        Initialize the EmotionRecognitionEngine with necessary models and configurations.
        """

        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        mp_path = os.path.join(base_path, 'mediapipe')
        os.environ["MEDIAPIPE_RESOURCE_DIR"] = mp_path

        self.model = self.load_model()
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.face_detection = self.mp_face_detection.FaceDetection(min_detection_confidence=0.5)
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.emotions = ['neutral', 'happiness', 'surprise', 'sadness', 'anger', 'disgust', 'fear', 'contempt']

        # Calibration factors and thresholds for emotion detection
        self.calibration_factors = {
            'neutral': 0.5, 'happiness': 0.5, 'surprise': 0.5, 'sadness': 0.5,
            'anger': 0.5, 'disgust': 0.5, 'fear': 0.5, 'contempt': 0.5
        }
        self.thresholds = {
            'neutral': 0.5, 'happiness': 0.5, 'surprise': 0.3, 'sadness': 0.01,
            'anger': 0.2, 'disgust': 0.01, 'fear': 0.0001, 'contempt': 0.0001
        }

        # Font settings for drawing text on the image
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 0.6
        self.font_thickness = 1
        self.text_color = (255, 255, 255)  # White color

        # Custom drawing spec for white face mesh
        self.custom_face_mesh_style = self.mp_drawing_styles.get_default_face_mesh_tesselation_style()
        self.custom_face_mesh_style.color = (194, 209, 194)
        self.custom_face_mesh_opacity = 0.08

    def load_model(self):
        """
        Load the TensorFlow Lite model for emotion recognition.

        Returns:
            tf.lite.Interpreter: The loaded TensorFlow Lite interpreter, or None if loading fails.
        """
        try:
            # Check if we're running in a PyInstaller bundle
            if getattr(sys, 'frozen', False):
                # If so, use the sys._MEIPASS path
                base_path = sys._MEIPASS
            else:
                # Get the directory of the current file
                base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            # Construct the path to the model file
            model_path = os.path.join(base_path, 'emotion_recognition', 'model', 'emotion_recognition_model.tflite')

            print(f"Attempting to load model from: {model_path}")

            if not os.path.exists(model_path):
                print(f"Error: Model file not found at {model_path}")
                return None

            interpreter = tf.lite.Interpreter(model_path=model_path)
            interpreter.allocate_tensors()
            print("Model loaded successfully")
            return interpreter
        except Exception as e:
            print(f"Error loading the model: {e}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            return None

    def process_frame(self, frame):
        """
        Process a single frame for emotion recognition.

        Args:
            frame (numpy.ndarray): The input frame to process.

        Returns:
            tuple: A tuple containing the processed frame (numpy.ndarray) and
                   a dictionary of detected emotions (or None if no face is detected).
        """
        if self.model is None:
            return frame, None

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face, face_coords = self.preprocess_image(rgb_frame)

        # Draw face mesh
        mesh_results = self.face_mesh.process(rgb_frame)
        if mesh_results.multi_face_landmarks:
            face_landmarks = mesh_results.multi_face_landmarks[0]
            self.draw_face_mesh(frame, face_landmarks)

        if face is not None:
            prediction = self.predict_emotion(face)

            emotions = {emotion: float(intensity) for emotion, intensity in zip(self.emotions, prediction)}

            x, y, w, h = face_coords
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            for i, (emo, prob) in enumerate(emotions.items()):
                text = f"{emo}: {int(prob * 100)}%"
                color = (0, 255, 0) if emo == max(emotions, key=emotions.get) else self.text_color
                cv2.putText(frame, text, (10, 30 + i * 25),
                            self.font, self.font_scale, color, self.font_thickness, cv2.LINE_AA)

            return frame, emotions
        else:
            cv2.putText(frame, "No face detected", (10, 30),
                        self.font, self.font_scale, (0, 0, 255), self.font_thickness, cv2.LINE_AA)
            return frame, None

    def draw_face_mesh(self, image, face_landmarks):
        """
        Draw the face mesh on the input image.

        Args:
            image (numpy.ndarray): The input image to draw on.
            face_landmarks: The face landmarks detected by MediaPipe.
        """
        # Create a semi-transparent overlay
        overlay = image.copy()

        # Draw the face mesh on the overlay
        self.mp_drawing.draw_landmarks(
            image=overlay,
            landmark_list=face_landmarks,
            connections=self.mp_face_mesh.FACEMESH_TESSELATION,
            landmark_drawing_spec=None,
            connection_drawing_spec=self.custom_face_mesh_style
        )

        # Blend the overlay with the original image
        alpha = self.custom_face_mesh_opacity
        cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

    def preprocess_image(self, image):
        """
        Preprocess the input image for emotion recognition.

        This method detects faces in the image and extracts the first detected face.

        Args:
            image (numpy.ndarray): The input RGB image.

        Returns:
            tuple: A tuple containing the preprocessed face image (numpy.ndarray) and
                   the face coordinates (tuple), or (None, None) if no face is detected.
        """
        results = self.face_detection.process(image)

        if results.detections:
            detection = results.detections[0]  # Get the first detected face
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                int(bboxC.width * iw), int(bboxC.height * ih)

            # Ensure the bounding box is within the image boundaries
            x, y = max(0, x), max(0, y)
            w = min(w, iw - x)
            h = min(h, ih - y)

            if w > 0 and h > 0:
                face = image[y:y + h, x:x + w]
                face = cv2.cvtColor(face, cv2.COLOR_RGB2GRAY)
                face = cv2.resize(face, (48, 48))
                face = face.astype('float32') / 255.0
                face = np.expand_dims(face, axis=-1)
                face = np.expand_dims(face, axis=0)
                return face, (x, y, w, h)

        return None, None

    def predict_emotion(self, face):
        """
        Predict emotions from a preprocessed face image.

        Args:
            face (numpy.ndarray): The preprocessed face image.

        Returns:
            numpy.ndarray: An array of calibrated emotion probabilities.
        """
        input_details = self.model.get_input_details()
        output_details = self.model.get_output_details()

        self.model.set_tensor(input_details[0]['index'], face)
        self.model.invoke()
        prediction = self.model.get_tensor(output_details[0]['index'])

        # Apply softmax to get probabilities
        exp_preds = np.exp(prediction[0])
        softmax_preds = exp_preds / np.sum(exp_preds)

        # Apply calibration factors
        calibrated_preds = softmax_preds * [self.calibration_factors[e] for e in self.emotions]
        calibrated_preds = calibrated_preds / np.sum(calibrated_preds)

        return calibrated_preds

    def cleanup(self):
        """
        Perform cleanup operations.

        This method should be called when the emotion recognition engine is no longer needed.
        It releases resources used by MediaPipe.
        """
        self.face_detection.close()
        self.face_mesh.close()