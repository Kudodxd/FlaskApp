from flask import Flask, render_template, url_for, current_app, g, request, redirect

# Install Flask class
app = Flask(__name__)
# Add SECRET_KEY
app.config["SECRET_KEY"] = "3425nkb4356nkb356kh235hk6"

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


with app.test_request_context():
    # /
    print(url_for("index"))
    # hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/minh?page=1
    print(url_for("show_name", name="minh", page="1"))
    # Output true
    print(request.args.get("updated"))

# print(current_app)

ctx = app.app_context()
ctx.push()

print(current_app.name)

g.connection = "connection"
print(g.connection)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/complete",
           methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # Get values from form
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # Send mail

        # Redirect to contact endpoint
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")
