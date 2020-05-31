import os
from flask import Flask
from flask_restful import Api

from resources.catalog_resource import CatalogResource
from resources.healthcheck_resource import HealthcheckResource

def api(app):
    """
    mount api based on app passed
    :param: none
    :return: none
    """ 

    api = Api(app)

    api.add_resource(CatalogResource, '/')
    api.add_resource(HealthcheckResource, '/healthcheck')

def app_factory(test_config=None):
    """
    create and configure the app
    :param test_config: param for application test configuration
    :return: object
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    api(app)

    return app
