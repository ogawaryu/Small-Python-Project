from flask_restful import Resource
from flask import request

from common.cube import get_volume_cube
from common.cylinder import get_volume_cylinder

class Geometry(Resource):
    def get(self):
        radius = request.args.get('radius')
        side = request.args.get('side')
        if radius and side:
            list_of_geometry = [
              { 'label': 'Volume of the Cube when the side is %s meters' % side, 'volume': get_volume_cube(side)},
              { 'label': 'Volume of the Cylinder when the radius is %s' % radius, 'volume': get_volume_cylinder(radius)}
            ]
            return list_of_geometry
        return None, 400
