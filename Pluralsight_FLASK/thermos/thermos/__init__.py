import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xca\x9a\x0e\x18k\x8c\x88\x94\xfe\xbb\x06\xaf\x9e/\x10^`#n\x1d\xd0v\xe5\xbb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
app.config['DEBUG'] = True
db = SQLAlchemy(app)

import models
import views