from PySide6.QtCore import QObject, Slot, Qt, QEvent
from PySide6.QtWidgets import QMessageBox, QDialog
from werkzeug.security import generate_password_hash, check_password_hash
from dialogs.ui.dialog_logout_after_profile_update import Ui_Dialog_LogoutAfterProfileUpdate


class SettingsController(QObject):
    """
    Controller class for managing user settings and profile updates.

    This class handles the logic for updating user profiles, including
    username and password changes, and manages the associated UI interactions.

    Attributes:
        main_window (QMainWindow): The main application window.
        settings_page (QWidget): The settings page widget.
        auth_service (AuthService): The authentication service.
        db_session (Session): The database session for performing database operations.
    """

    def __init__(self, main_window):
        """
        Initialize the SettingsController.

        Args:
            main_window (QMainWindow): The main application window.
        """
        super().__init__()
        self.main_window = main_window
        self.settings_page = main_window.settings_page
        self.auth_service = main_window.auth_service
        self.db_session = main_window.get_db_session()

        # Connect signals
        self.settings_page.pushButton_Save.clicked.connect(self.OnClick_pushButton_Save)
        self.settings_page.pushButton_Cancel.clicked.connect(self.OnClick_pushButton_Cancel)

        # Load current user data
        self.load_user_data()

        # Event filter for Enter key press
        self.settings_page.lineEdit_Username.installEventFilter(self)
        self.settings_page.lineEdit_CurrentPassword.installEventFilter(self)
        self.settings_page.lineEdit_NewPassword.installEventFilter(self)
        self.settings_page.lineEdit_ConfirmNewPassword.installEventFilter(self)

        # Clear all error messages initially
        self.clear_error_messages()

    def eventFilter(self, obj, event):
        """
        Filter events for the settings page input fields.

        This method captures Enter key presses in the input fields and triggers
        the save action.

        Args:
            obj (QObject): The object that triggered the event.
            event (QEvent): The event that occurred.

        Returns:
            bool: True if the event was handled, False otherwise.
        """
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
            if obj in [self.settings_page.lineEdit_Username,
                       self.settings_page.lineEdit_CurrentPassword,
                       self.settings_page.lineEdit_NewPassword,
                       self.settings_page.lineEdit_ConfirmNewPassword]:
                self.OnClick_pushButton_Save()
            return True
        return super().eventFilter(obj, event)

    def load_user_data(self):
        """
        Load the current user's data into the settings page.
        """
        current_user = self.main_window.get_current_user()
        if current_user:
            self.settings_page.lineEdit_Username.setText(current_user.username)

    @Slot()
    def OnClick_pushButton_Save(self):
        """
        Handle the save button click event.

        This method validates the user input, updates the user profile,
        and handles any necessary logout procedures.
        """
        current_user = self.main_window.get_current_user()
        if not current_user:
            QMessageBox.warning(self.main_window, "Error", "No user logged in.")
            return

        new_username = self.settings_page.lineEdit_Username.text().strip()
        current_password = self.settings_page.lineEdit_CurrentPassword.text()
        new_password = self.settings_page.lineEdit_NewPassword.text()
        confirm_new_password = self.settings_page.lineEdit_ConfirmNewPassword.text()

        # Clear previous error messages
        self.clear_error_messages()

        # Validate inputs
        if not self.validate_inputs(new_username, current_password, new_password, confirm_new_password):
            return

        # Verify current password
        if not check_password_hash(current_user.password_hash, current_password):
            self.settings_page.label_ErrorMessageForCurrentPassword.setText("*Incorrect current password*")
            self.settings_page.lineEdit_CurrentPassword.setFocus()
            return

        # Update username if changed
        username_changed = False
        if new_username != current_user.username:
            if self.auth_service.is_username_taken(new_username):
                self.settings_page.label_ErrorMessageForUsername.setText("*Username already taken*")
                self.settings_page.lineEdit_Username.setFocus()
                return
            current_user.username = new_username
            username_changed = True

        # Update password if changed
        password_changed = False
        if new_password != current_password:
            current_user.password_hash = generate_password_hash(new_password)
            password_changed = True

        # Save changes
        try:
            self.db_session.commit()
            self.clear_password_fields()

            # Show logout dialog and handle logout if username or password changed
            if username_changed or password_changed:
                self.show_logout_dialog()
            else:
                self.settings_page.label_SuccessUpdateMessage.setText("Profile updated successfully!")
        except Exception as e:
            self.db_session.rollback()
            QMessageBox.warning(self.main_window, "Error", f"Failed to update profile: {str(e)}")

    def show_logout_dialog(self):
        """
        Show a dialog informing the user that they need to log out after profile changes.
        """
        self.main_window.blur_background()

        dialog = QDialog(self.main_window)
        ui = Ui_Dialog_LogoutAfterProfileUpdate()
        ui.setupUi(dialog)

        # Connect the accepted and rejected signals
        dialog.accepted.connect(self.logout_user)
        dialog.rejected.connect(self.logout_user)

        dialog.exec()

        self.main_window.unblur_background()

    def logout_user(self):
        """
        Log out the current user and update the UI accordingly.
        """
        # Deactivate emotion recognition if active
        if self.main_window.emotion_recognition_controller:
            self.main_window.auth_service.logout_user(self.main_window.user_session.user)
            self.main_window.clear_user_session()

            # Cleanup emotion recognition resources
            if self.main_window.emotion_recognition_controller:
                self.main_window.emotion_recognition_controller.cleanup()
                self.main_window.emotion_recognition_controller = None

            self.main_window.showUsers()
            self.main_window.update_nav_visibility()

        current_user = self.main_window.get_current_user()
        if current_user:
            self.auth_service.logout_user(current_user)
            self.main_window.clear_user_session()
            self.main_window.showUsers()
            self.main_window.update_nav_visibility()

    def validate_inputs(self, username, current_password, new_password, confirm_new_password):
        """
        Validate user inputs for profile update.

        Args:
            username (str): The new username.
            current_password (str): The current password.
            new_password (str): The new password.
            confirm_new_password (str): The confirmation of the new password.

        Returns:
            bool: True if all inputs are valid, False otherwise.
        """
        is_valid = True

        if not username:
            self.settings_page.label_ErrorMessageForUsername.setText("*Username cannot be empty*")
            self.settings_page.lineEdit_Username.setFocus()
            is_valid = False

        if not current_password:
            self.settings_page.label_ErrorMessageForCurrentPassword.setText("*Current password cannot be empty*")
            if is_valid:
                self.settings_page.lineEdit_CurrentPassword.setFocus()
            is_valid = False

        if not new_password:
            self.settings_page.label_ErrorMessageForNewPassword.setText("*New password cannot be empty*")
            if is_valid:
                self.settings_page.lineEdit_NewPassword.setFocus()
            is_valid = False
        elif len(new_password) < 8:
            self.settings_page.label_ErrorMessageForNewPassword.setText(
                "*New password must be at least 8 characters long*")
            if is_valid:
                self.settings_page.lineEdit_NewPassword.setFocus()
            is_valid = False
        elif new_password == current_password:
            self.settings_page.label_ErrorMessageForNewPassword.setText(
                "*New password must be different from current password*")
            if is_valid:
                self.settings_page.lineEdit_NewPassword.setFocus()
            is_valid = False

        if not confirm_new_password:
            self.settings_page.label_ErrorMessageForConfirmNewPassword.setText("*Confirm new password cannot be empty*")
            if is_valid:
                self.settings_page.lineEdit_ConfirmNewPassword.setFocus()
            is_valid = False
        elif new_password != confirm_new_password:
            self.settings_page.label_ErrorMessageForConfirmNewPassword.setText("*Passwords do not match*")
            if is_valid:
                self.settings_page.lineEdit_ConfirmNewPassword.setFocus()
            is_valid = False

        return is_valid

    @Slot()
    def OnClick_pushButton_Cancel(self):
        """
        Handle the cancel button click event.

        This method clears all input fields and reloads the current user data.
        """
        self.clear_fields()
        self.load_user_data()

    def clear_fields(self):
        """
        Clear all input fields and error messages in the settings page.
        """
        self.clear_password_fields()
        self.clear_error_messages()
        self.settings_page.label_SuccessUpdateMessage.clear()

    def clear_password_fields(self):
        """
        Clear all password-related input fields in the settings page.
        """
        self.settings_page.lineEdit_CurrentPassword.clear()
        self.settings_page.lineEdit_NewPassword.clear()
        self.settings_page.lineEdit_ConfirmNewPassword.clear()

    def clear_error_messages(self):
        """
        Clear all error message labels in the settings page.
        """
        self.settings_page.label_ErrorMessageForUsername.clear()
        self.settings_page.label_ErrorMessageForCurrentPassword.clear()
        self.settings_page.label_ErrorMessageForNewPassword.clear()
        self.settings_page.label_ErrorMessageForConfirmNewPassword.clear()

    def clear_messages(self):
        """
        Clear all error messages and success messages in the settings page.
        """
        self.clear_error_messages()
        self.settings_page.label_SuccessUpdateMessage.clear()


if __name__ == "__main__":
    import sys
    from main import main

    sys.argv.append("settings")
    main()