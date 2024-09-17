from PySide6.QtCore import QObject, Qt
from PySide6.QtWidgets import QLabel, QApplication, QFrame, QHBoxLayout


class UsersController(QObject):
    """
    Controller class for handling user list operations and UI interactions.
    """

    def __init__(self, main_window, auth_service):
        """
        Initialize the UsersController.

        Args:
            main_window: The main window of the application.
            auth_service (AuthService): The authentication service to use for user-related operations.
        """
        super().__init__()
        self.main_window = main_window
        self.auth_service = auth_service
        self.users_page = main_window.users_page

        # Load users from database
        self.load_users()

        # Connect UI elements
        self.users_page.pushButton_CreateAnAccount.clicked.connect(self.OnClick_pushButton_CreateAnAccount)

    def load_users(self):
        """
        Load users from the database and display them in the UI.
        """
        users = self.auth_service.get_users()

        # Clear existing user frames
        while self.users_page.usersLayout.count():
            child = self.users_page.usersLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        if users:
            self.users_page.label_SelectUsername.setText("Select your username below to log in")
            for user in users:
                self.add_user_to_ui(user)
        else:
            self.users_page.label_SelectUsername.setText("No users found. Create an account below")

        # Add a stretch at the end to push everything to the top
        self.users_page.usersLayout.addStretch(1)

        # Force the layout to update
        self.users_page.usersContainer.updateGeometry()

    def update_user_frame(self, frame, user):
        """
        Update the user frame with the latest user information.

        Args:
            frame (QFrame): The frame to update.
            user (User): The user object containing the updated information.
        """
        username_label = frame.findChild(QLabel, "label_Username")
        last_active_label = frame.findChild(QLabel, "label_LastActiveDate")

        username_label.setText(user.username)
        last_active_label.setText(f"Last active on {user.last_active.strftime('%m/%d/%Y at %I:%M%p')}")

        frame.mousePressEvent = lambda event, u=user: self.OnClick_User(u)

    def add_user_to_ui(self, user):
        """
        Add a user to the UI by creating a new user frame.

        Args:
            user (User): The user object to add to the UI.
        """
        user_frame = QFrame(self.users_page.usersContainer)
        user_frame.setObjectName(f"frame_{user.username}")
        user_frame.setStyleSheet("""
            background-color: #fff;
            border: 1px solid #f5f5f5;
            border-radius: 10px;
            padding-left: 10px;
            padding-right: 10px;
            margin-bottom:3px;
        """)
        user_frame.setFrameShape(QFrame.StyledPanel)
        user_frame.setFrameShadow(QFrame.Raised)

        layout = QHBoxLayout(user_frame)

        username_label = QLabel(user.username, user_frame)
        username_label.setStyleSheet("border: none;")
        layout.addWidget(username_label)

        last_active_label = QLabel(f"Last active on {user.last_active.strftime('%m/%d/%Y at %I:%M%p')}", user_frame)
        last_active_label.setStyleSheet("border: none;")
        last_active_label.setAlignment(Qt.AlignRight)
        layout.addWidget(last_active_label)

        user_frame.mousePressEvent = lambda event, u=user: self.OnClick_User(u)

        self.users_page.usersLayout.addWidget(user_frame)

    def OnClick_User(self, user):
        """
        Handle user frame click event.
        Navigates to the login page for the selected user.

        Args:
            user (User): The user object associated with the clicked frame.
        """
        self.main_window.showLogin()
        self.main_window.login_page.label_WelcomeMessage.setText(f"Glad you're back <b>{user.preferred_name}</b>!")
        self.main_window.login_controller.set_current_username(user.username)

    def OnClick_pushButton_CreateAnAccount(self):
        """
        Handle create an account button click event.
        Navigates to the first page of the registration process.
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

    sys.argv.append("users")
    main()