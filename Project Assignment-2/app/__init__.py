from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = 'ff127ef745c8859dd6509413570a5bd3'
app.config["SQLALCHEMY_DATABASE_URI"] = '' #AWS RDS URI
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'login1'

from app import routes
