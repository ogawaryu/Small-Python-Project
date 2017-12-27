from flask import Flask
from flask_restful import Api
from api.cube import Cube
from api.cylinder import Cylinder
from api.geometry import Geometry

app = Flask(__name__)
api = Api(app)

api.add_resource(Cube, '/cube')
api.add_resource(Cylinder, '/cylinder')
api.add_resource(Geometry, '/geometry')

def flaskrun():
    return app