"""Specify configurations"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Base configuration
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                 '7b0342f12ee64296aaaa9738c72ca2c4'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql://user:password@localhost:5432/department_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """
    Testing configuration
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                 '1c666j11esd5296kh6s12090cc1cff1l8'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'department_app/tests/test.db')
