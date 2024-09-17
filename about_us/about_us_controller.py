from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget

class AboutUsController(QObject):
    """ Controller class for the About Us page of the EmoSense application.

    This class manages the content and behavior of the About Us page.

    Attributes:
        main_window (QWidget): The main window of the application.
        about_us_page (QWidget): The About Us page widget.
    """

    def __init__(self, main_window):
        """ Initialize the AboutUsController.

        Args:
            main_window (QWidget): The main window of the application.
        """
        super().__init__()
        self.main_window = main_window
        self.about_us_page = main_window.about_us_page

        # Set the content for the About Us page
        self.set_about_us_content()

    def set_about_us_content(self):
        """ Set the content for the About Us page.

        This method defines and sets the HTML content for the About Us page,
        including information about EmoSense, its features, and benefits.
        """
        about_us_text = """
        <h2>Welcome to EmoSense: Your Intelligent Companion for Emotional Well-Being</h2>

        <p>EmoSense is an innovative offline emotion recognition software designed to be your personal companion for emotional insights and well-being. Our mission is to help you understand and manage your emotions better, leading to improved mental health and overall life satisfaction.</p>

        <h3>Our Vision</h3>
        <p>At EmoSense, we envision a world where everyone has access to tools that enhance emotional intelligence and promote mental well-being. We believe that understanding and managing our emotions is key to leading happier, more fulfilling lives and building stronger relationships.</p>

        <h3>Key Features:</h3>
        <ul>
            <li><strong>AI-Powered Emotion Recognition:</strong> Utilizing advanced artificial intelligence and computer vision technology, EmoSense analyzes your facial expressions in real-time to identify and monitor your emotions. Our sophisticated algorithms can detect subtle changes in your expression, providing accurate insights into your emotional state.</li>
            <li><strong>Discreet Background Operation:</strong> EmoSense works quietly in the background, ensuring your privacy while providing valuable emotional insights. You can go about your daily computer activities without interruption, knowing that EmoSense is there to support your emotional well-being.</li>
            <li><strong>Comprehensive Mood Analytics:</strong> Receive daily, weekly, and monthly summaries of your emotional states, helping you track patterns and trends in your mood over time. These insights can help you identify triggers, understand your emotional rhythms, and make informed decisions about your lifestyle and habits.</li>
            <li><strong>Personalized Well-Being Strategies:</strong> Benefit from tailored mood management techniques and activity recommendations. EmoSense learns from your patterns and preferences to suggest activities, exercises, or practices that can help improve your mood and overall well-being.</li>
            <li><strong>Complete Privacy:</strong> Your emotional data never leaves your device. All processing, analysis, and storage happen locally, ensuring that your sensitive information remains completely private and secure.</li>
        </ul>

        <h3>How EmoSense Works</h3>
        <p>EmoSense uses your computer's camera to capture video frames in real-time. Our advanced AI algorithms analyze these frames to detect facial expressions and map them to emotional states. This data is then processed to provide you with real-time feedback, long-term trends, and personalized recommendations.</p>

        <p>The app operates entirely offline, ensuring that all your data remains on your device.</p>

        <h3>Benefits of Using EmoSense</h3>
        <ul>
            <li>Increased self-awareness and emotional intelligence</li>
            <li>Better understanding of your emotional patterns and triggers</li>
            <li>Improved stress management and mood regulation</li>
            <li>Enhanced personal and professional relationships through better emotional understanding</li>
            <li>Personalized strategies for maintaining and improving mental well-being</li>
            <li>A private, judgment-free space for emotional exploration and growth</li>
        </ul>

        <h3>Our Commitment to You</h3>
        <p>At EmoSense, we are committed to your privacy, security, and well-being. We continuously work on improving our algorithms and expanding our feature set to provide you with the most accurate, helpful, and user-friendly emotional companion possible.</p>

        <p>We believe that everyone deserves access to tools that support their emotional health. That's why we've made EmoSense completely offline and accessible, ensuring that you can benefit from advanced emotional insights without concerns about data privacy or constant internet connectivity.</p>

        <h3>Join Us on Your Journey to Emotional Well-Being</h3>
        <p>Whether you're looking to improve your emotional intelligence, manage stress better, or simply gain a deeper understanding of your emotional patterns, EmoSense is here to support you every step of the way.</p>

        <p>Start your journey towards better emotional understanding and well-being with EmoSense today. Let's work together to create a more emotionally intelligent and empathetic world, one person at a time.</p>

        <p>Thank you for choosing EmoSense as your companion on this important journey. We're excited to be part of your path to enhanced emotional well-being and personal growth.</p>
        """

        # Set the HTML content to the label in the About Us page
        self.about_us_page.label_AboutUsContent.setText(about_us_text)

if __name__ == "__main__":
    import sys
    from main import main

    # Append "about_us" to sys.argv to indicate that we want to show the About Us page
    sys.argv.append("about_us")
    # Call the main function to start the application
    main()