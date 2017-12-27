from flask_restful import Resource
from flask import request
from common.cylinder import get_volume_cylinder

class Cylinder(Resource):
    def get(self):
        radius = request.args.get('radius')
        if radius:
            volume = get_volume_cylinder(radius)
            return {
              'label': 'Volume of the Cylinder when the radius is %s' % radius,
              'volume': volume
            }
        return None, 400
