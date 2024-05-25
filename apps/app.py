# from pathlib import Path
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from apps.config import config

# Object db
db = SQLAlchemy()

csrf = CSRFProtect()

login_manager = LoginManager()
# Specify endpoint to redirect when not logged in
login_manager.login_view = "auth.signup"
# Specify message that show when logged in
login_manager.login_message = ""


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

    login_manager.init_app(app)
    # Import views from crud package
    # Register crud of view to the app using register_blueprint
    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # Register auth of views
    from apps.auth import views as auth_views

    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    # Register dt(detector)
    from apps.detector import views as dt_views

    app.register_blueprint(dt_views.dt)

    return app
