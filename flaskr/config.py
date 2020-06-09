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
