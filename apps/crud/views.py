from flask import (
    Blueprint,
    render_template,
)

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
