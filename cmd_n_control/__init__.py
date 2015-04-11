from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
db.init_app(app)

import cmd_n_control.views
import cmd_n_control.models


