from flask_restful import Resource
from flask import request
from common.cube import get_volume_cube

class Cube(Resource):
    def get(self):
        side = request.args.get('side')
        if side:
            volume = get_volume_cube(side)
            return {
              'label': 'Volume of the Cube when the side is %s meters' % side,
              'volume': volume
            }
        return None, 400
