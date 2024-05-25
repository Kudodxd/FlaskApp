from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from apps.app import db
from apps.auth.forms import LoginForm, SignUpForm
from apps.crud.models import User

auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@auth.route("/")
def index():
    return render_template("auth/index.html")


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # Create user
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        if user.is_duplicate_email():
            flash("Email is already taken")
            return redirect(url_for("auth.signup"))

        # Add user and commit
        db.session.add(user)
        db.session.commit()

        login_user(user)

        next_ = request.args.get("next")
        if next_ is None or not next_.startswith("/"):
            next_ = url_for("crud.users")
        return redirect(next_)

    return render_template("auth/signup.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for("detector.index"))

        # Login failed
        flash("Password is wrong!.")
    return render_template("auth/login.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
