from flask import render_template, url_for, flash, redirect
from app import app, bcrypt, db
from app.forms import RegistrationForm, LoginForm1, LoginForm2, Info, Picture
from app.models import User, UserInfo
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    pic_fn = random_hex + f_ext
    pic_path = os.path.join(app.root_path, 'static', 'profile_pictures', pic_fn)
    form_picture.save(pic_path)
    return pic_fn
    


@app.route('/')
@app.route('/home')
def home():
    db.create_all()
    return render_template("main.html", title=None, user=None)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/registration", methods=["GET", "POST"])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for("home", title=None))
    form = RegistrationForm()
    if form.validate_on_submit():
        app.logger.info("All information valid")
        temp_var = form.username.data
        hash_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data\
            , email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()

        user = User.query.filter_by(username=temp_var).first()
        app.logger.warning(str(user.id))
        info = UserInfo(about="", link1=None, link2=None, link3=None, link4=None, profession=None, recovery_mail=None, user_id=user.id)
        db.session.add(info)
        db.session.commit()
        flash('Account created for {}'.format(form.username.data), 'success') 
        return redirect(url_for('login1'))
    else:
        app.logger.warning(str([error for error in form.errors]) + " form elements have error")
    return render_template("registration.html", title="Sign Up", form=form)

@app.route("/login-username", methods=["GET", "POST"])
def login1():
    if current_user.is_authenticated:
        return redirect(url_for("home", title=None))
    form = LoginForm1()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home', title=None, user=user))
        else:
            flash('Login unsuccessful. Please check username and password.', 'danger')
    return render_template("username-login.html", title="Login", form=form)

@app.route("/login-email", methods=["GET", "POST"])
def login2():
    if current_user.is_authenticated:
        return redirect(url_for("home", title=None))
    form = LoginForm2()
    if form.validate_on_submit():
        app.logger.info("All information valid")
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home', title=None, user=user))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template("email-login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home", title=None))

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = Picture()
    info = UserInfo.query.filter_by(id=current_user.id).first()
    if form.validate_on_submit():
        if form.profile.data:
            pic_file = save_picture(form.profile.data)
            info.profile = pic_file
            db.session.commit()
    return render_template("account.html", title="Account", form=form)

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = Info()
    if form.validate_on_submit():
        info = UserInfo.query.filter_by(id=current_user.id).first()
        app.logger.warning("User Id: " + str(info.id) + " Professtion: " + str(info.profession))
        info.about = form.about.data
        info.link1 = form.link1.data
        info.link2 = form.link2.data
        info.link3 = form.link3.data
        info.link4 = form.link4.data
        info.profession = form.profession.data
        info.recovery_mail = form.recovery_mail.data
        db.session.commit()
        return render_template("account.html", title="Account")
    return render_template("profile.html", title="Edit Profile", form=form)