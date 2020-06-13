import os


class Config:
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    # DB_SERVER = '192.168.1.56'


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    """Uses production database server."""
    # DB_SERVER = '192.168.19.32'
    pass


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DB_SERVER = 'lc_db:27017'
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    SQLALCHEMY_DATABASE_URI = f"postgres://{POSTGRES_USER}:" \
                              f"{POSTGRES_PASSWORD}@lc_db:5432/db_local"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    DB_SERVER = 'localhost'
    DEBUG = True
    # DATABASE_URI = 'sqlite:///:memory:'


config = {
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "default": "config.DevelopmentConfig"
}
