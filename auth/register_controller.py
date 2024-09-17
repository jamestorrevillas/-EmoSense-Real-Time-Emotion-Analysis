from PySide6.QtCore import QObject, Qt, QEvent
from PySide6.QtWidgets import QApplication
from session.user_session import UserSession


class RegisterController(QObject):
    """
    Controller class for handling user registration operations and UI interactions.
    """

    def __init__(self, main_window, auth_service):
        """
        Initialize the RegisterController.

        Args:
            main_window: The main window of the application.
            auth_service (AuthService): The authentication service to use for user registration.
        """
        super().__init__()
        self.main_window = main_window
        self.auth_service = auth_service
        self.user_session = UserSession()
        self.register_page_1 = main_window.register_page_1
        self.register_page_2 = main_window.register_page_2
        self.main_window.resetElementFields()
        self.register_page_1.label_DateOfBirth.setText(f"<b>Date of Birth <span style='font-weight: normal;'>("
                                                       f"dd/mm/yyyy)</span><b/>")

        # Connect UI elements for page 1 to their respective functions
        self.register_page_1.pushButton_Next.clicked.connect(self.OnClick_pushButton_Next)
        self.register_page_1.pushButton_GoBack.clicked.connect(self.OnClick_pushButton_GoBackPage1)

        # Connect UI elements for page 2 to their respective functions
        self.register_page_2.pushButton_CreateAccount.clicked.connect(self.OnClick_pushButton_CreateAccount)
        self.register_page_2.pushButton_GoBack.clicked.connect(self.OnClick_pushButton_GoBackPage2)

        # Install event filters for Enter key press on Register Page 1
        self.register_page_1.lineEdit_PreferredName.installEventFilter(self)
        self.register_page_1.comboBox_Gender.installEventFilter(self)
        self.register_page_1.dateEdit_DateOfBirth.installEventFilter(self)

        # Install event filters for Enter key press on Register Page 2
        self.register_page_2.lineEdit_Username.installEventFilter(self)
        self.register_page_2.lineEdit_Password.installEventFilter(self)
        self.register_page_2.lineEdit_ConfirmPassword.installEventFilter(self)

    def eventFilter(self, obj, event):
        """
        Event filter to handle Enter key press in registration form fields.

        Args:
            obj (QObject): The object that triggered the event.
            event (QEvent): The event that occurred.

        Returns:
            bool: True if the event was handled, False otherwise.
        """
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
            if obj in [self.register_page_1.lineEdit_PreferredName,
                       self.register_page_1.comboBox_Gender,
                       self.register_page_1.dateEdit_DateOfBirth]:
                self.OnClick_pushButton_Next()
            elif obj in [self.register_page_2.lineEdit_Username,
                         self.register_page_2.lineEdit_Password,
                         self.register_page_2.lineEdit_ConfirmPassword]:
                self.OnClick_pushButton_CreateAccount()
            return True
        return super().eventFilter(obj, event)

    def OnClick_pushButton_CreateAccount(self):
        """
        Handle create account button click event.
        Validates user input and creates a new user account if all inputs are valid.
        """
        username = self.register_page_2.lineEdit_Username.text()
        password = self.register_page_2.lineEdit_Password.text()
        confirm_password = self.register_page_2.lineEdit_ConfirmPassword.text()

        # Clear all error messages initially
        self.register_page_2.label_ErrorMessageForUsername.setText(None)
        self.register_page_2.label_ErrorMessageForPassword.setText(None)
        self.register_page_2.label_ErrorMessageForConfirmPassword.setText(None)

        # Validation for Register Page 2
        if not username:
            self.register_page_2.label_ErrorMessageForUsername.setText("*Username cannot be empty*")
            self.register_page_2.lineEdit_Username.setFocus()
            return

        if not password:
            self.register_page_2.label_ErrorMessageForPassword.setText("*Password cannot be empty*")
            self.register_page_2.lineEdit_Password.setFocus()
            return
        elif len(password) < 8:
            self.register_page_2.label_ErrorMessageForPassword.setText("*Password must be at least 8 characters long*")
            self.register_page_2.lineEdit_Password.setFocus()
            return

        if not confirm_password:
            self.register_page_2.label_ErrorMessageForConfirmPassword.setText("*Please confirm your password*")
            self.register_page_2.lineEdit_ConfirmPassword.setFocus()
            return
        elif password != confirm_password:
            self.register_page_2.label_ErrorMessageForConfirmPassword.setText("*Passwords do not match*")
            self.register_page_2.lineEdit_ConfirmPassword.setFocus()
            return

        # If all validations pass, attempt to register the user
        preferred_name = self.register_page_1.lineEdit_PreferredName.text()
        gender = self.register_page_1.comboBox_Gender.currentText()
        date_of_birth = self.register_page_1.dateEdit_DateOfBirth.date().toString("yyyy-MM-dd")

        if self.auth_service.register_user(preferred_name, gender, date_of_birth, username, password):
            user = self.auth_service.verify_user(username, password)
            if user:
                self.user_session.user = user
                self.main_window.showHome()
                self.main_window.resetElementFields()
        else:
            self.register_page_2.label_ErrorMessageForUsername.setText("*Username already exists*")
            self.register_page_2.lineEdit_Username.setFocus()

    def OnClick_pushButton_Next(self):
        """
        Handle next button click event on Register Page 1.
        Validates user input on the first registration page and moves to the second page if all inputs are valid.
        """
        preferred_name = self.register_page_1.lineEdit_PreferredName.text()
        gender = self.register_page_1.comboBox_Gender.currentText()
        date_of_birth = self.register_page_1.dateEdit_DateOfBirth.date().toString("yyyy-MM-dd")

        # Clear all error messages initially
        self.register_page_1.label_ErrorMessageForPreferredName.setText(None)
        self.register_page_1.label_ErrorMessageForGender.setText(None)
        self.register_page_1.label_ErrorMessageForDateOfBirth.setText(None)

        # Validation for Register Page 1
        if not preferred_name:
            self.register_page_1.label_ErrorMessageForPreferredName.setText("*Preferred name cannot be empty*")
            self.register_page_1.lineEdit_PreferredName.setFocus()
            return

        if not gender or self.register_page_1.comboBox_Gender.currentIndex() == 0:
            self.register_page_1.label_ErrorMessageForGender.setText("*Please select a gender*")
            self.register_page_1.comboBox_Gender.setFocus()
            return

        if not date_of_birth or date_of_birth == "1900-01-01":
            self.register_page_1.label_ErrorMessageForDateOfBirth.setText("*Please enter a valid date of birth*")
            self.register_page_1.dateEdit_DateOfBirth.setFocus()
            return

        # If all validations pass, move to the next page
        self.main_window.showRegisterPage2()

    def OnClick_pushButton_GoBackPage1(self):
        """
        Handle go back button click event on Register Page 1.
        Returns to the users page.
        """
        self.main_window.showUsers()

    def OnClick_pushButton_GoBackPage2(self):
        """
        Handle go back button click event on Register Page 2.
        Returns to Register Page 1.
        """
        self.main_window.showRegisterPage1()

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
        sys.argv.append("register_page_1")
        main()