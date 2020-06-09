from flask_restful import Resource
from typing import Tuple


class HealthcheckResource(Resource):
    """ class that checks the health of the application"""
    def get(self) -> Tuple[str, int]:
        return 'Working', 200
