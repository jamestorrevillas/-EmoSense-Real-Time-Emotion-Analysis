from datetime import datetime
import pytz

from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from sqlalchemy.exc import IntegrityError

from models.user import Gender, AccountStatus


class AuthService:
    """
    Service class for handling user authentication and registration.
    """

    def __init__(self, db_session):
        """
        Initialize the AuthService.

        Args:
            db_session: The database session to use for database operations.
        """
        self.db_session = db_session

    def register_user(self, preferred_name, gender_str, date_of_birth_str, username, password):
        """
        Register a new user in the system.

        Args:
            preferred_name (str): The user's preferred name.
            gender_str (str): The user's gender as a string.
            date_of_birth_str (str): The user's date of birth as a string in 'YYYY-MM-DD' format.
            username (str): The desired username for the new user.
            password (str): The password for the new user.

        Returns:
            bool: True if registration was successful, False otherwise.

        Raises:
            IntegrityError: If there's a database integrity error (e.g., duplicate username).
            ValueError: If there's an error in gender enum conversion or date parsing.
        """
        try:
            # Convert gender string to enum
            gender = Gender[gender_str.upper().replace(" ", "_")]

            # Convert date string to Python date object
            date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d").date()

            # Create a new User object with the provided information
            new_user = User(
                username=username,
                preferred_name=preferred_name,
                gender=gender,
                date_of_birth=date_of_birth,
                created_at=datetime.now(pytz.timezone('UTC')).astimezone(),  # Local time
                last_active=datetime.now(pytz.timezone('UTC')).astimezone(),
                account_status=AccountStatus.ACTIVE,
                password_hash=generate_password_hash(password)
            )
            self.db_session.add(new_user)
            self.db_session.commit()
            return True
        except IntegrityError:
            # Roll back the session if there's an integrity error (e.g., duplicate username)
            self.db_session.rollback()
            return False
        except ValueError as e:
            # This will catch errors in gender enum conversion or date parsing
            print(f"Error in user data: {str(e)}")
            return False

    def verify_user(self, username, password):
        """
        Verify a user's credentials and update their status.

        Args:
            username (str): The username of the user to verify.
            password (str): The password to check against the stored hash.

        Returns:
            User: The verified User object if credentials are correct, None otherwise.
        """
        user = self.db_session.query(User).filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            # Update user's last active time and status
            user.last_active = datetime.now()
            user.account_status = AccountStatus.ACTIVE
            self.db_session.commit()
            return user
        return None

    def get_users(self):
        """
        Retrieve all users from the database, ordered by last active time.

        Returns:
            list: A list of all User objects, sorted by last_active in descending order.
        """
        return self.db_session.query(User).order_by(User.last_active.desc()).all()

    def logout_user(self, user):
        """
        Log out a user by updating their last active time and status.

        Args:
            user (User): The User object to log out.
        """
        user.last_active = datetime.now()
        user.account_status = AccountStatus.INACTIVE
        self.db_session.commit()

    def is_username_taken(self, username):
        """
        Check if a username is already taken.

        Args:
            username (str): The username to check.

        Returns:
            bool: True if the username is taken, False otherwise.
        """
        user = self.db_session.query(User).filter_by(username=username).first()
        return user is not None