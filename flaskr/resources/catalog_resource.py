from flask_restful import Resource


class CatalogResource(Resource):
    def get(self):
        return {'hello': 'world'}