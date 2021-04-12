from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = 'ff127ef745c8859dd6509413570a5bd3'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://lkhcaehjtjrbmi:c2e2b58de522d95c1bd8d490f0d278aaf023233c074569403206f8a724e8a6cd@ec2-54-167-168-52.compute-1.amazonaws.com:5432/d678c8ni4pc6mo'
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'login1'

from app import routes