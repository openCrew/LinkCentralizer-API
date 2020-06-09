from flask_restful import Resource, partial, reqparse
from typing import Tuple, Dict, List
from facade import catalog_facade


class CatalogResource(Resource):
    def get(self) -> Tuple[Dict[str, str], int]:
        """
        here is the get method documentation
        :return:
        """
        return {'hello': 'catalog'}, 200

    @staticmethod
    def post() -> Tuple[Dict[str, str], int]:
        """
        here is the POST method documentation
        :return:
        """
        pass
