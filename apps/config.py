from pathlib import Path

basedir = Path(__file__).parent.parent


class BaseConfig:
    SECRET_KEY = "24h5jh25j52GJV%UTGV&G%23"
    WTF_CSRF_SECRET_KEY = "Asdauif4ihv89nsib26d"


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = (False,)
    # Output console log of SQL
    SQLALCHEMY_ECHO = (True,)


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = (False,)
    WTF_CSRF_ENABLED = False


config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}
