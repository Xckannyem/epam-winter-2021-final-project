
import unittest
from department_app import create_app, db
from config import TestingConfig


class BaseTestCase(unittest.TestCase):
    """
    Base test case class
    """
    def setUp(self):
        """
        Execute before every test case
        """
        self.app = create_app()
        self.app.config.from_object(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """
        Execute after every test case
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
