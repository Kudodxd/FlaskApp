from flask import (
    Flask,
    render_template,
    url_for,
    # current_app,
    # g,
    request,
    redirect,
    flash,
    make_response,
    session,
)
from email_validator import (
    validate_email,
    EmailNotValidError,
)
# Mail function
from flask_mail import (
    Mail,
    Message,
)
# Debug toolbar
from flask_debugtoolbar import DebugToolbarExtension
import logging
import os

app = Flask(__name__)
# Add SECRET_KEY for session -> why must use session? -> to export flash messages
app.config["SECRET_KEY"] = "3425nkb4356nkb356kh235hk6"

# Setup log level
app.logger.setLevel(logging.DEBUG)
# app.logger.critical("fatal error")
# app.logger.error("error")
# app.logger.warning("warning")
# app.logger.info("info")
# app.logger.debug("debug")

# For not interupting redirect
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

# DebugToolbarExtension
toolbar = DebugToolbarExtension(app)

# Add config for class Mail
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

# Register flask-mail
mail = Mail(app)


# Mapping function that excutes with URL
@app.route("/",
           methods=["GET", "POST"])
def index():
    return "Hello, Flaskbook!"


@app.route("/hello/<name>",
           methods=["GET", "POST"],
           endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!"


# Create a show-name endpoint
@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)


# with app.test_request_context():
#     # /
#     print(url_for("index"))

#     # hello/world
#     print(url_for("hello-endpoint", name="world"))

#     # /name/minh?page=1
#     print(url_for("show_name", name="minh", page="1"))

#     # Output true
#     print(request.args.get("updated"))

# print(current_app)

# ctx = app.app_context()
# ctx.push()

# print(current_app.name)

# g.connection = "connection"
# print(g.connection)


@app.route("/contact")
def contact():
    # Create a respone object
    respone = make_response(render_template("contact.html"))

    # Setup cookie
    respone.set_cookie("Flaskbook key", "flaskbook value")

    # Setup session
    session["username"] = "minh"
    return respone


@app.route("/contact/complete",
           methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # Get values from form
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # Check input
        is_valid = True

        if not username:
            flash("Username is required.")
            is_valid = False

        if not email:
            flash("Email is required.")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("Please enter in email address format.")
            is_valid = False

        if not description:
            flash("Inquiry details are required.")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        # Send mail
        send_email(
            email,
            "Thank you for your contact.",
            "contact_mail",
            username=username,
            description=description,
        )
        # Redirect to contact endpoint
        flash("Thank you for your contact. Inquiry details had been send")
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")


def send_email(to, subject, template, **kwagrs):
    """Functions to send mail"""
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwagrs)
    msg.html = render_template(template + ".html", **kwagrs)
    mail.send(msg)
