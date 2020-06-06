from flask_restful import Resource
from typing import Tuple


class HealthcheckResource(Resource):
    def get(self) -> Tuple[str, int]:
        return 'Working', 200