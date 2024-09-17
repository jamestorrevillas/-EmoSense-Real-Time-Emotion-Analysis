import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base


class Database:
    """ A class to manage database operations for the EmoSense application.

    This class provides methods to create a database connection, create tables,
    and manage database sessions using SQLAlchemy.

    Attributes:
        engine (sqlalchemy.engine.base.Engine): The SQLAlchemy engine instance.
        Session (sqlalchemy.orm.session.sessionmaker): A session factory for creating new sessions.
    """

    def __init__(self, db_name='emosense.db'):
        """ Initialize the Database class.

        Args:
            db_name (str, optional): The name of the database file. Defaults to 'emosense.db'.
        """
        # Determine the correct base directory
        if getattr(sys, 'frozen', False):
            # If the application is run as a bundle, use the sys._MEIPASS
            base_dir = sys._MEIPASS
        else:
            # If running from a script, use the script's directory
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Construct the full path to the database directory
        db_dir = os.path.join(base_dir, 'database')

        # Create the database directory if it doesn't exist
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)

        # Construct the full path to the database file
        self.db_path = os.path.join(db_dir, db_name)

        # Create a SQLAlchemy engine for SQLite
        self.engine = create_engine(f'sqlite:///{self.db_path}')

        # Create a sessionmaker bound to this engine
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        """ Create all tables defined in the SQLAlchemy models.

        This method should be called once when setting up the database for the first time.
        """
        Base.metadata.create_all(self.engine)

    def get_session(self):
        """ Create and return a new SQLAlchemy session.

        Returns:
            sqlalchemy.orm.session.Session: A new SQLAlchemy session object.
        """
        return self.Session()

    def get_db_path(self):
        """Get the full path to the database file.

        This method is useful for debugging purposes.

        Returns:
            str: The full path to the database file.
        """
        return self.db_path

    def initialize_database(self):
        """Initialize the database if it doesn't exist."""
        if not os.path.exists(self.db_path):
            self.create_tables()
            print(f"Database initialized at: {self.db_path}")
        else:
            print(f"Database already exists at: {self.db_path}")