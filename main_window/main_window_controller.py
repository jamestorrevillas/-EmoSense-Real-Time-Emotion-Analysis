from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QDialog, QSystemTrayIcon, QMenu, QApplication, \
    QGraphicsBlurEffect

from main_window.ui.main_window import Ui_MainWindow
from auth.ui.users import Ui_UsersForm
from auth.ui.login import Ui_LoginForm
from auth.ui.register_page_1 import Ui_RegisterFormWindow1
from auth.ui.register_page_2 import Ui_RegisterFormWindow2
from about_us.ui.about_us import Ui_AboutUsWindow
from home.ui.home import Ui_HomeWindow
from emotion_recognition.ui.emotion_recognition import Ui_EmotionRecognitionWindow
from emotion_analytics.ui.emotion_analytics import Ui_EmotionAnalyticsWindow
from settings.ui.settings import Ui_SettingsFormWindow
from dialogs.ui.dialog_confirm_exit import Ui_Dialog_ConfirmExit
from dialogs.ui.dialog_confirm_logout import Ui_Dialog_ConfirmLogout

from auth.users_controller import UsersController
from auth.login_controller import LoginController
from auth.register_controller import RegisterController
from about_us.about_us_controller import AboutUsController
from home.home_controller import HomeController
from emotion_recognition.emotion_recognition_controller import EmotionRecognitionController
from emotion_analytics.emotion_analytics_controller import EmotionAnalyticsController
from settings.settings_controller import SettingsController
from dialogs.exit_dialog_controller import ExitDialogController
from assets.animations.controller.animation_controller import AnimationController

from database.database import Database
from auth.auth_service import AuthService
from models.user import AccountStatus
from session.user_session import UserSession
from sqlalchemy.orm import sessionmaker


class MainWindowController(QMainWindow):
    """
    Main controller for the application window.
    Manages the overall UI, navigation, and integrates various components.
    """

    def __init__(self):
        """
        Initialize the MainWindowController.
        Sets up the main window UI, database connection, and various UI components.
        """
        super().__init__()
        self.user_session = UserSession()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize database
        self.db = Database()
        self.db_session = self.db.get_session()
        self.auth_service = AuthService(self.db_session)

        # Create a session factory
        self.Session = sessionmaker(bind=self.db.engine)

        # Set up window style
        self.setWindowTitle("EmoSense")
        self.setStyleSheet("background-color: #FFF;")
        self.setWindowIcon(QIcon(":/icons/images/icons/logo.png"))

        # Initialize UI forms for different screens
        self._initialize_ui_forms()

        # Create screen widgets
        self._create_screen_widgets()

        # Set up individual pages
        self._setup_individual_pages()

        # Add screen widgets to the stacked widget
        self._add_widgets_to_stack()

        # Initialize controllers for each screen
        self._initialize_controllers()

        # Set up navigation buttons
        self._setup_navigation()

        # Set up users page
        self._setup_users_page()

        self.animation_controller = AnimationController(self)

        # Set up system tray
        self.setup_system_tray()

        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(0)
        self.ui.stackedWidget.setGraphicsEffect(self.blur_effect)

        self.emotion_recognition_controller = None
        self.is_closing = False

    def _initialize_ui_forms(self):
        """Initialize UI form objects for different screens."""
        self.users_page = Ui_UsersForm()
        self.login_page = Ui_LoginForm()
        self.register_page_1 = Ui_RegisterFormWindow1()
        self.register_page_2 = Ui_RegisterFormWindow2()
        self.about_us_page = Ui_AboutUsWindow()
        self.home_page = Ui_HomeWindow()
        self.emotion_recognition_page = Ui_EmotionRecognitionWindow()
        self.emotion_analytics_page = Ui_EmotionAnalyticsWindow()
        self.settings_page = Ui_SettingsFormWindow()

    def _create_screen_widgets(self):
        """Create QWidget objects for each screen."""
        self.users_widget = QWidget()
        self.login_widget = QWidget()
        self.register_page_1_widget = QWidget()
        self.register_page_2_widget = QWidget()
        self.about_us_widget = QWidget()
        self.home_widget = QWidget()
        self.emotion_recognition_widget = QWidget()
        self.emotion_analytics_widget = QWidget()
        self.settings_widget = QWidget()

    def _setup_individual_pages(self):
        """Set up UI for individual pages."""
        self.users_page.setupUi(self.users_widget)
        self.login_page.setupUi(self.login_widget)
        self.register_page_1.setupUi(self.register_page_1_widget)
        self.register_page_2.setupUi(self.register_page_2_widget)
        self.about_us_page.setupUi(self.about_us_widget)
        self.home_page.setupUi(self.home_widget)
        self.emotion_recognition_page.setupUi(self.emotion_recognition_widget)
        self.emotion_analytics_page.setupUi(self.emotion_analytics_widget)
        self.settings_page.setupUi(self.settings_widget)

    def _add_widgets_to_stack(self):
        """Add screen widgets to the stacked widget."""
        self.ui.stackedWidget.addWidget(self.users_widget)
        self.ui.stackedWidget.addWidget(self.login_widget)
        self.ui.stackedWidget.addWidget(self.register_page_1_widget)
        self.ui.stackedWidget.addWidget(self.register_page_2_widget)
        self.ui.stackedWidget.addWidget(self.about_us_widget)
        self.ui.stackedWidget.addWidget(self.home_widget)
        self.ui.stackedWidget.addWidget(self.emotion_recognition_widget)
        self.ui.stackedWidget.addWidget(self.emotion_analytics_widget)
        self.ui.stackedWidget.addWidget(self.settings_widget)

    def _initialize_controllers(self):
        """Initialize controllers for each screen."""
        self.users_controller = UsersController(self, self.auth_service)
        self.login_controller = LoginController(self, self.auth_service)
        self.register_controller = RegisterController(self, self.auth_service)
        self.about_us_controller = AboutUsController(self)
        self.home_controller = HomeController(self)
        self.emotion_recognition_controller = EmotionRecognitionController(self)
        self.emotion_analytics_controller = EmotionAnalyticsController(self)
        self.settings_controller = SettingsController(self)

    def _setup_navigation(self):
        """Set up navigation button event handlers."""
        self.ui.label_Home.mousePressEvent = self.showHome
        self.ui.label_RealTimeEmotion.mousePressEvent = self.showRealTimeEmotion
        self.ui.label_EmotionAnalytics.mousePressEvent = self.showEmotionAnalytics
        self.ui.label_Settings.mousePressEvent = self.showSettings
        self.ui.label_AboutUs.mousePressEvent = self.showAboutUs
        self.ui.label_Login.mousePressEvent = self.showUsers
        self.ui.label_Logout.mousePressEvent = self.logout
        self.ui.label_Close.mousePressEvent = self.show_exit_dialog

    def _setup_users_page(self):
        """Set up the users page layout."""
        if self.users_page.usersContainer.layout():
            QWidget().setLayout(self.users_page.usersContainer.layout())
        self.users_page.usersLayout = QVBoxLayout(self.users_page.usersContainer)
        self.users_page.usersLayout.setAlignment(Qt.AlignTop)
        self.users_page.usersLayout.setContentsMargins(0, 0, 0, 0)
        self.users_page.usersLayout.setSpacing(0)
        if self.users_page.frame_User:
            self.users_page.frame_User.setParent(None)

        self.users_controller.load_users()

    def resizeEvent(self, event):
        """
        Handle the resize event of the main window.

        Args:
            event (QResizeEvent): The resize event object.
        """
        super().resizeEvent(event)
        if hasattr(self, 'emotion_analytics_controller'):
            self.emotion_analytics_controller.on_main_window_resize(event)

    def showUsers(self, event=None):
        """
        Show the users page.

        Args:
            event (QMouseEvent, optional): The mouse event that triggered this method.
        """
        self.update_nav_visibility()
        self.update_nav_styles("Login")
        self.animation_controller.switch_and_fade_in(self.users_widget)
        self.users_controller.load_users()

    def showLogin(self, event=None):
        """
        Show the login page.

        Args:
            event (QMouseEvent, optional): The mouse event that triggered this method.
        """
        self.update_nav_visibility()
        self.update_nav_styles("Login")
        self.animation_controller.switch_and_fade_in(self.login_widget)
        self.login_page.lineEdit_Password.setFocus()

    def showRegisterPage1(self, event=None):
        """
        Show the first registration page.

        Args:
            event (QMouseEvent, optional): The mouse event that triggered this method.
        """
        self.update_nav_visibility()
        self.update_nav_styles("Login")
        self.animation_controller.switch_and_fade_in(self.register_page_1_widget)
        self.register_page_1.lineEdit_PreferredName.setFocus()

    def showRegisterPage2(self, event=None):
        """
        Show the second registration page.

        Args:
            event (QMouseEvent, optional): The mouse event that triggered this method.
        """
        self.update_nav_visibility()
        self.update_nav_styles("Login")
        self.animation_controller.switch_and_fade_in(self.register_page_2_widget)
        self.register_page_2.lineEdit_Username.setFocus()

    def showAboutUs(self, event=None):
        """
        Show the About Us page.

        Args:
            event (QMouseEvent, optional): The mouse event that triggered this method.
        """
        self.update_nav_visibility()
        self.update_nav_styles("AboutUs")
        self.animation_controller.switch_and_fade_in(self.about_us_widget)

    def showHome(self, event=None):
        """
        Show the Home page.

        Args:
            event (QMouseEvent, optional): The mouse event that triggered this method.
        """
        self.update_nav_visibility()
        self.update_nav_styles("Home")
        self.animation_controller.switch_and_fade_in(self.home_widget)

    def showRealTimeEmotion(self, event=None):
        """
        Show the Real-Time Emotion Recognition page.

        Args:
            event (QMouseEvent, optional): The mouse event that triggered this method.
        """
        self.update_nav_visibility()
        self.update_nav_styles("RealTimeEmotion")
        if self.emotion_recognition_controller is None:
            self.emotion_recognition_controller = EmotionRecognitionController(self)
        self.emotion_recognition_controller.populate_camera_sources()
        self.animation_controller.switch_and_fade_in(self.emotion_recognition_widget)

    def showEmotionAnalytics(self, event=None):
        """
        Show the Emotion Analytics page.

        Args:
            event (QMouseEvent, optional): The mouse event that triggered this method.
        """
        self.update_nav_visibility()
        self.update_nav_styles("EmotionAnalytics")
        if self.is_user_authenticated():
            self.emotion_analytics_controller.initialize_ui()
        else:
            self.emotion_analytics_controller.display_no_user_message()
        self.animation_controller.switch_and_fade_in(self.emotion_analytics_widget)

    def showSettings(self, event=None):
        """
        Show the Settings page.

        Args:
            event (QMouseEvent, optional): The mouse event that triggered this method.
        """
        self.update_nav_visibility()
        self.update_nav_styles("Settings")
        self.animation_controller.switch_and_fade_in(self.settings_widget)
        self.settings_controller.load_user_data()
        self.settings_controller.clear_messages()

    def logout(self, event=None):
        """
        Handle user logout.

        Args:
            event (QMouseEvent, optional): The mouse event that triggered this method.
        """
        if self.user_session.user:
            self.blur_background()

            confirm_logout_dialog = QDialog(self)
            ui = Ui_Dialog_ConfirmLogout()
            ui.setupUi(confirm_logout_dialog)

            result = confirm_logout_dialog.exec()

            if result == QDialog.DialogCode.Accepted:
                self.auth_service.logout_user(self.user_session.user)
                self.clear_user_session()

                # Cleanup emotion recognition resources
                if self.emotion_recognition_controller:
                    self.emotion_recognition_controller.cleanup()
                    self.emotion_recognition_controller = None

                self.showUsers()
                self.update_nav_visibility()

            self.unblur_background()

    def show_exit_dialog(self, event=None):
        """
        Show the exit confirmation dialog.

        Args:
            event (QMouseEvent, optional): The mouse event that triggered this method.
        """
        self.handle_exit()

    def blur_background(self):
        """Apply a blur effect to the background."""
        self.blur_effect.setBlurRadius(10)
        self.ui.centralwidget.setGraphicsEffect(self.blur_effect)

    def unblur_background(self):
        """Remove the blur effect from the background."""
        self.blur_effect.setBlurRadius(0)
        self.ui.stackedWidget.setGraphicsEffect(self.blur_effect)

    def setup_system_tray(self):
        """Set up the system tray icon and menu."""
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(":/icons/images/icons/logo.png"))

        tray_menu = QMenu()
        show_action = tray_menu.addAction("Show")
        show_action.triggered.connect(self.show)
        exit_action = tray_menu.addAction("Exit")
        exit_action.triggered.connect(self.close_app)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def close_app(self):
        """
        Close the application and perform necessary cleanup.
        """
        # Perform any necessary cleanup
        if self.emotion_recognition_controller:
            self.emotion_recognition_controller.cleanup()
            self.emotion_recognition_controller = None

        # Set the flag to indicate we're closing the app
        self.is_closing = True

        # Close the application
        QApplication.quit()

    def closeEvent(self, event):
        """
        Handle the window close event.

        Args:
            event (QCloseEvent): The close event object.
        """
        if self.is_closing:
            event.accept()  # Allow the close event if we're deliberately closing
        else:
            event.ignore()  # Ignore the close event
            self.handle_exit()

    def handle_exit(self):
        """
        Handle the exit process, showing appropriate dialogs based on the application state.
        """
        self.blur_background()

        is_emotion_recognition_active = (
                self.emotion_recognition_controller is not None and
                self.emotion_recognition_controller.custom_toggle_camera.isChecked() and
                self.emotion_recognition_controller.custom_toggle_activate.isChecked()
        )

        if is_emotion_recognition_active:
            exit_dialog = ExitDialogController(self)
            result = exit_dialog.exec()

            if result == QDialog.DialogCode.Accepted:
                action = exit_dialog.get_selected_action()
                if action == "minimize":
                    self.hide()
                    self.tray_icon.showMessage("EmoSense", "Application minimized to system tray",
                                               QSystemTrayIcon.Information, 2000)
                elif action == "exit":
                    self.close_app()
        else:
            confirm_exit_dialog = QDialog(self)
            ui = Ui_Dialog_ConfirmExit()
            ui.setupUi(confirm_exit_dialog)
            result = confirm_exit_dialog.exec()

            if result == QDialog.DialogCode.Accepted:
                self.close_app()

        self.unblur_background()

    def is_user_authenticated(self):
        """
        Check if a user is currently authenticated.

        Returns:
            bool: True if a user is authenticated and active, False otherwise.
        """
        return self.user_session.user is not None and self.user_session.user.account_status == AccountStatus.ACTIVE

    def get_db_session(self):
        """
        Get a new database session.

        Returns:
            Session: A new SQLAlchemy database session.
        """
        return self.Session()

    def save_to_db(self, obj):
        """
        Save an object to the database.

        Args:
            obj: The object to be saved to the database.
        """
        session = self.get_db_session()
        session.add(obj)
        session.commit()
        session.close()

    def get_current_user(self):
        """
        Get the currently logged-in user.

        Returns:
            User: The current user object, or None if no user is logged in.
        """
        user = self.user_session.user
        return user

    def get_current_user_id(self):
        """
        Get the ID of the currently logged-in user.

        Returns:
            int: The ID of the current user.
        """
        return self.get_current_user().id

    def set_current_user(self, user):
        """
        Set the current user in the session.

        Args:
            user (User): The user object to set as the current user.
        """
        self.user_session.user = user

    def clear_user_session(self):
        """
        Clear the current user session.
        """
        self.user_session.clear()

    def update_nav_visibility(self):
        """
        Update the visibility of navigation elements based on user authentication status.
        """
        self.ui.label_Home.setVisible(self.is_user_authenticated())
        self.ui.label_RealTimeEmotion.setVisible(self.is_user_authenticated())
        self.ui.label_EmotionAnalytics.setVisible(self.is_user_authenticated())
        self.ui.label_Settings.setVisible(self.is_user_authenticated())
        self.ui.label_Login.setVisible(not self.is_user_authenticated())
        self.ui.label_Logout.setVisible(self.is_user_authenticated())
        # Update other navigation elements as needed

    def resetElementFields(self):
        """
        Reset all input fields and error messages in the UI.
        """
        # Reset registration page 1 fields
        self.register_page_1.lineEdit_PreferredName.setText(None)
        self.register_page_1.label_ErrorMessageForPreferredName.setText(None)
        self.register_page_1.label_ErrorMessageForGender.setText(None)
        self.register_page_1.label_ErrorMessageForDateOfBirth.setText(None)
        self.register_page_1.comboBox_Gender.setCurrentIndex(0)
        self.register_page_1.dateEdit_DateOfBirth.setDate(QDate(1900, 1, 1))

        # Reset registration page 2 fields
        self.register_page_2.lineEdit_Username.setText(None)
        self.register_page_2.lineEdit_Password.setText(None)
        self.register_page_2.lineEdit_ConfirmPassword.setText(None)
        self.register_page_2.label_ErrorMessageForUsername.setText(None)
        self.register_page_2.label_ErrorMessageForPassword.setText(None)
        self.register_page_2.label_ErrorMessageForConfirmPassword.setText(None)

        # Reset login page fields
        self.login_page.lineEdit_Password.setText(None)
        self.login_page.label_ErrorMessage.setText(None)

        # Reset emotion recognition page fields
        self.emotion_recognition_page.label_ErrorMessageForCameraSettings.setText(None)

    def update_nav_styles(self, current_page):
        """
        Update the styles of navigation elements based on the current page.

        Args:
            current_page (str): The identifier of the current page.
        """
        nav_labels = {
            "Home": self.ui.label_Home,
            "RealTimeEmotion": self.ui.label_RealTimeEmotion,
            "EmotionAnalytics": self.ui.label_EmotionAnalytics,
            "Settings": self.ui.label_Settings,
            "AboutUs": self.ui.label_AboutUs,
            "Login": self.ui.label_Login,
            "Logout": self.ui.label_Logout
        }

        for page, label in nav_labels.items():
            if page == current_page:
                label.setStyleSheet("""
                    QLabel {
                        background-color: #FFF;
                        color: #000;
                        border: none;
                        font-weight: bold;
                    }
                    QLabel:hover {
                        color: #011BA1;
                    }
                """)
            else:
                label.setStyleSheet("""
                    QLabel {
                        background-color: #FFF;
                        color: #000;
                        border: none;
                        font-weight: normal;
                    }
                    QLabel:hover {
                        color: #011BA1;
                    }
                """)