from flask import Flask

app = Flask(__name__)

from department_app import routes
