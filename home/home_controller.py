from PySide6.QtCore import QObject


class HomeController(QObject):
    """ Controller for the home page of the EmoSense application.

    This class manages the home page UI and its interactions.

    Args:
        main_window: The main window of the application.
    """

    def __init__(self, main_window):
        """ Initialize the HomeController.

        Args:
            main_window: The main window of the application.
        """
        super().__init__()
        self.main_window = main_window
        self.home_page = main_window.home_page

        # Set the content for the home page
        self.set_home_content()

        # Connect UI elements for unauthenticated page
        self.home_page.pushButton_ActivateNow.clicked.connect(self.OnClick_pushButton_ActivateNow)

    def set_home_content(self):
        """ Set the content for the home page.

        This method defines and sets the HTML content for the home page,
        including information about EmoSense, its features, and benefits.
        """
        home_content = """
        <h2>Discover the Power of Emotional Intelligence with EmoSense</h2>

        <p>Welcome to EmoSense, your intelligent companion for real-time emotion insights and well-being. In today's fast-paced world, understanding and managing our emotions is more crucial than ever. EmoSense is here to help you navigate your emotional landscape with ease and precision.</p>

        <h3>What is EmoSense?</h3>
        <p>EmoSense is a cutting-edge, offline emotion recognition software that uses advanced AI and computer vision technology to analyze your facial expressions in real-time. By providing instant feedback on your emotional state, EmoSense helps you develop greater self-awareness and emotional intelligence.</p>

        <h3>Key Features of EmoSense:</h3>
        <ul>
            <li><strong>Real-time Emotion Recognition:</strong> Our sophisticated algorithms detect and analyze your facial expressions as you use your computer, providing immediate insights into your emotional state.</li>
            <li><strong>Privacy-First Approach:</strong> EmoSense operates entirely offline, ensuring that your emotional data never leaves your device.</li>
            <li><strong>Comprehensive Analytics:</strong> Gain valuable insights into your emotional patterns with daily, weekly, and monthly summaries.</li>
            <li><strong>Personalized Well-being Strategies:</strong> Receive tailored recommendations to improve your mood and overall emotional well-being.</li>
        </ul>

        <h3>How EmoSense Works:</h3>
        <p>EmoSense uses your computer's camera to capture video frames in real-time. Our AI algorithms then analyze these frames to detect facial expressions and map them to emotional states. This data is processed locally on your device to provide you with instant feedback and long-term trends.</p>

        <h3>Benefits of Using EmoSense:</h3>
        <ul>
            <li>Enhance your emotional intelligence and self-awareness</li>
            <li>Identify emotional patterns and triggers</li>
            <li>Improve stress management and mood regulation</li>
            <li>Boost personal and professional relationships through better emotional understanding</li>
            <li>Track your emotional well-being over time</li>
            <li>Receive personalized strategies for maintaining and improving mental health</li>
        </ul>

        <h3>Getting Started with EmoSense</h3>
        <p>To begin your journey towards better emotional understanding, simply click the "Activate Now" button below. EmoSense will guide you through a quick setup process, and you'll be on your way to discovering valuable insights about your emotional well-being.</p>

        <p>Remember, emotional intelligence is a skill that can be developed and refined over time. With EmoSense as your companion, you're taking an important step towards a more emotionally aware and fulfilling life.</p>

        <p>We're excited to be part of your emotional well-being journey. Let's explore the world of emotions together with EmoSense!</p>
        """

        # Set the HTML content to the home page label
        self.home_page.label_HomeContent.setText(home_content)

    def OnClick_pushButton_ActivateNow(self):
        """ Handle the 'Activate Now' button click event.

        This method is called when the user clicks the 'Activate Now' button.
        It initializes the real-time emotion recognition feature and handles
        camera setup.

        Raises:
            None, but displays an error message if no camera is detected.
        """
        # Switch to the real-time emotion recognition page
        self.main_window.showRealTimeEmotion()

        # Get the EmotionRecognitionController instance
        emotion_recognition_controller = self.main_window.emotion_recognition_controller

        # Populate camera sources if not already done
        if not emotion_recognition_controller.camera_sources_populated:
            emotion_recognition_controller.populate_camera_sources()

        # Check if a camera is available
        if emotion_recognition_controller.emotion_recognition_page.comboBox_CameraSource.count() > 0:
            # Turn on the camera
            emotion_recognition_controller.custom_toggle_camera.setChecked(True)

            # Turn on emotion recognition
            emotion_recognition_controller.custom_toggle_activate.setChecked(True)
        else:
            # Show an error message if no camera is available
            emotion_recognition_controller.emotion_recognition_page.label_ErrorMessageForCameraSettings.setText(
                "No camera detected. Please connect a camera and try again.")


if __name__ == "__main__":
    import sys
    from main import main

    # Add 'home' argument to sys.argv for testing purposes
    sys.argv.append("home")
    main()