import os
import sys
from PySide6.QtWidgets import QApplication
from main_window.main_window_controller import MainWindowController
from database.database import Database  # Add this import

def main():
    """
    Main entry point of the application.

    This function initializes the application, sets up environment variables,
    and handles command-line arguments to determine the initial screen to display.

    Args:
        None

    Returns:
        None

    Raises:
        SystemExit: When the application execution is complete.
    """
    # Set environment variables to suppress TensorFlow warnings and use legacy Keras
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    os.environ["TF_USE_LEGACY_KERAS"] = "1"

    # Initialize the database
    db = Database()
    db.initialize_database()  # Add this line to initialize the database

    # Initialize the Qt application
    app = QApplication(sys.argv)
    main_controller = MainWindowController()

    # Check if a start screen is specified in command-line arguments
    if len(sys.argv) > 1:
        start_screen = sys.argv[1]
        # Map command-line arguments to corresponding controller methods
        screen_map = {
            "users": main_controller.showUsers,
            "login": main_controller.showLogin,
            "register_page_1": main_controller.showRegisterPage1,
            "register_page_2": main_controller.showRegisterPage2,
            "about_us": main_controller.showAboutUs,
            "home": main_controller.showHome,
            "emotion_recognition": main_controller.showRealTimeEmotion,
            "emotion_analytics": main_controller.showEmotionAnalytics,
            "settings": main_controller.showSettings
        }

        # Call the appropriate method based on the start_screen argument
        if start_screen in screen_map:
            screen_map[start_screen]()
        else:
            # If an invalid screen is specified, default to users screen
            main_controller.showUsers()
    else:
        # If no start screen is specified, default to users screen
        main_controller.showUsers()

    # Display the main window maximized
    main_controller.showMaximized()

    # Start the application event loop and exit when it's done
    sys.exit(app.exec())

if __name__ == "__main__":
    main()