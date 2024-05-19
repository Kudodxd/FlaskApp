from flask import (
    Flask,
)


def create_app():
    # Create Flask instance
    app = Flask(__name__)

    # Import views from crud package
    from apps.crud import views as crud_views

    # Register crud of view to the app using register_blueprint
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app
