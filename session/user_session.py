class UserSession:
    """
    A singleton class to manage the current user session.

    This class ensures that only one instance of UserSession exists
    throughout the application, maintaining a single point of access
    for the current user information.

    Attributes:
        _instance (UserSession): The single instance of the UserSession class.
        current_user (Any): The currently logged-in user object.
    """

    _instance = None

    def __new__(cls):
        """
        Create a new instance of UserSession if it doesn't exist, otherwise return the existing one.

        Returns:
            UserSession: The single instance of the UserSession class.
        """
        if cls._instance is None:
            cls._instance = super(UserSession, cls).__new__(cls)
            cls._instance.current_user = None
        return cls._instance

    @property
    def user(self):
        """
        Get the current user.

        Returns:
            Any: The current user object or None if no user is logged in.
        """
        return self.current_user

    @user.setter
    def user(self, user):
        """
        Set the current user.

        Args:
            user (Any): The user object to set as the current user.
        """
        self.current_user = user

    def clear(self):
        """
        Clear the current user session.

        This method is typically called when a user logs out.
        """
        self.current_user = None