import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

basedir = os.path.abspath(os.path.dirname(__file__))


# Configure database
app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
app.config['DEBUG'] = True
db = SQLAlchemy(app)

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

# enable debugtoolbar
toolbar = DebugToolbarExtension(app)

# for displaying timestamps
moment = Moment(app)

# Own module imports
import thermos.models
import thermos.views