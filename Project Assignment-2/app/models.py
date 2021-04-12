from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), unique=False, nullable=True)
    last_name = db.Column(db.String(40), unique=False, nullable=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    account_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    info = db.relationship('UserInfo', backref='info', lazy=True)

    def __repr__(self):
        return "User details - Name: {}, Username: {}, Email: {}".format(self.first_name + " " + self.last_name, self.username, self.email)


class UserInfo(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    about = db.Column(db.String(750), unique=False, nullable=True)
    link1 = db.Column(db.String(500), unique=False, nullable=True)
    link2 = db.Column(db.String(500), unique=False, nullable=True)
    link3 = db.Column(db.String(500), unique=False, nullable=True)
    link4 = db.Column(db.String(500), unique=False, nullable=True)
    profession = db.Column(db.String(100), unique=False, nullable=True)
    profile = db.Column(db.String(100), unique=False, nullable=True, default='profile.png')
    recovery_mail = db.Column(db.String(100), unique=False, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)

    def __repr__(self):
        return "Profession - {} Id- {}".format(self.profession, self.id)