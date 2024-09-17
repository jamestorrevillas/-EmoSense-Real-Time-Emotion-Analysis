from PySide6.QtCore import QObject, Qt, QEvent
from PySide6.QtWidgets import QApplication
from session.user_session import UserSession


class LoginController(QObject):
    """
    Controller class for handling login-related operations and UI interactions.
    """

    def __init__(self, main_window, auth_service):
        """
        Initialize the LoginController.

        Args:
            main_window: The main window of the application.
            auth_service (AuthService): The authentication service to use for user verification.
        """
        super().__init__()
        self.main_window = main_window
        self.auth_service = auth_service
        self.user_session = UserSession()
        self.login_page = main_window.login_page
        self.main_window.resetElementFields()
        self.current_username = None

        # Connect buttons to their respective functions
        self.login_page.pushButton_Login.clicked.connect(self.OnClick_pushButton_Login)
        self.login_page.pushButton_GoBack.clicked.connect(self.OnClick_pushButton_GoBack)

        # Install event filter on password input field to handle Enter key press
        self.login_page.lineEdit_Password.installEventFilter(self)

    def set_current_username(self, username):
        """
        Set the current username for login.

        Args:
            username (str): The username to set.
        """
        self.current_username = username

    def eventFilter(self, obj, event):
        """
        Event filter to handle Enter key press in the password field.

        Args:
            obj (QObject): The object that triggered the event.
            event (QEvent): The event that occurred.

        Returns:
            bool: True if the event was handled, False otherwise.
        """
        if obj == self.login_page.lineEdit_Password and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                self.OnClick_pushButton_Login()
                return True
        return super().eventFilter(obj, event)

    def OnClick_pushButton_Login(self):
        """
        Handle login button click event.
        Verifies user credentials and logs in the user if valid.
        """
        password = self.login_page.lineEdit_Password.text()
        if not password:
            self.login_page.label_ErrorMessage.setText("*Password cannot be empty*")
        elif self.current_username:
            user = self.auth_service.verify_user(self.current_username, password)
            if user:
                self.user_session.user = user
                self.main_window.showHome()
                self.main_window.resetElementFields()
            else:
                self.login_page.label_ErrorMessage.setText("*Invalid password*")

    def OnClick_pushButton_GoBack(self):
        """
        Handle go back button click event.
        Returns to the users page.
        """
        self.main_window.showUsers()

    def OnClick_label_AboutUs(self, event):
        """
        Handle about us label click event.
        Shows the about us page.

        Args:
            event: The click event (unused, but kept for consistency with Qt signal/slot mechanism).
        """
        self.main_window.showAboutUs()

    def OnClick_label_Close(self, event):
        """
        Handle close label click event.
        Quits the application.

        Args:
            event: The click event (unused, but kept for consistency with Qt signal/slot mechanism).
        """
        QApplication.quit()


if __name__ == "__main__":
    import sys
    from main import main
    sys.argv.append("login")
    main()