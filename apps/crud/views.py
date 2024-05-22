from flask import Blueprint, redirect, render_template, url_for

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
def index():
    return render_template("crud/index.html")


@crud.route("/sql")
def sql():
    # db.session.query(User).all()
    # db.session.query(User).first()
    # db.session.query(User).get(2)
    # db.session.query(User).count()
    db.session.query(User).paginate(page=2, per_page=10)
    User.query.filter_by(id=2, username="admin").all()
    return "Please confirm console log"


@crud.route("/users/new", methods=["GET", "POST"])
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
        return redirect(url_for("/crud.users"))
    return render_template("crud/create.html", form=form)
