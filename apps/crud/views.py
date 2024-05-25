from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required

from apps.app import db
from apps.crud.forms import UserForm
from apps.crud.models import User

# Create CRUD app using Blueprint
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)


# Create index endpoint and return index.html
@crud.route("/")
@login_required
def index():
    return render_template("crud/index.html")


@crud.route("/sql")
@login_required
def sql():
    # db.session.query(User).all()
    # db.session.query(User).first()
    # db.session.query(User).get(2)
    # db.session.query(User).count()
    db.session.query(User).paginate(page=2, per_page=10)
    User.query.filter_by(id=2, username="admin").all()
    return "Please confirm console log"


@crud.route("/users/new", methods=["GET", "POST"])
@login_required
def create_user():
    # Instance UserForm
    form = UserForm()
    # Validate form's value
    if form.validate_on_submit():
        # Create user
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        # Add user and commit
        db.session.add(user)
        db.session.commit()
        # Redirect to user HP
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)


@crud.route("/users")
@login_required
def users():
    """User list"""
    users = User.query.all()
    return render_template("crud/index.html", users=users)


@crud.route("/users/<user_id>", methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    form = UserForm()

    # Filtering user using User model
    user = User.query.filter_by(id=user_id).first()

    # Submiting form means update user and redirects to Users table
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))

    # if method is GET then return edit.html
    return render_template("crud/edit.html", user=user, form=form)


@crud.route("/users/<user_id>/delete", methods=["POST"])
@login_required
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))
