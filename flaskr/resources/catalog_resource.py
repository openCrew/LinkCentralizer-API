from flask_restful import Resource
from typing import Tuple, Dict
from facade import catalog_facade


class CatalogResource(Resource):
    def get(self) -> Tuple[Dict[str, str], int]:
        return {'hello': 'catalog'}, 200

    def post(self) -> None:
        pass
