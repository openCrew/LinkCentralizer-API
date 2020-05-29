from flask_restful import Resource


class Catalog(Resource):
    def get(self):
        return {'hello': 'world'}