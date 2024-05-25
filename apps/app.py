# from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from apps.config import config

# Object db
db = SQLAlchemy()

csrf = CSRFProtect()


def create_app(config_key):
    # Create Flask instance
    app = Flask(__name__)

    # Setup app config by form_object. Read config class for each env
    app.config.from_object(config[config_key])

    # # Setup app config by form_mapping
    # app.config.from_mapping(
    #     SECRET_KEY="2AZSMss3p5QPbcY2hBs",
    #     SQLALCHEMY_DATABASE_URI="sqlite:///"
    #     + str(Path(Path(__file__).parent.parent, "local.sqlite")),
    #     SQLALCHEMY_TRACK_MODIFICATIONS=False,
    #     # Output console log of SQL
    #     SQLALCHEMY_ECHO=True,
    #     WTF_CSRF_SECRET_KEY="Aewurfgiasaljdc27b24rhid",
    # )

    csrf.init_app(app)

    # Align app to SQLAlchemy
    db.init_app(app)

    # Align app to Migrate
    Migrate(app, db)

    # Import views from crud package
    from apps.crud import views as crud_views

    # Register crud of view to the app using register_blueprint
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app
