from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Object db
db = SQLAlchemy()


def create_app():
    # Create Flask instance
    app = Flask(__name__)

    # Setup app config
    app.config.from_mapping(
        SECRET_KEY="23h234gj23jgh42v3jgh",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # Align app to SQLAlchemy
    db.init_app(app)

    # Align app to Migrate
    Migrate(app, db)

    # Import views from crud package
    from apps.crud import views as crud_views

    # Register crud of view to the app using register_blueprint
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app
