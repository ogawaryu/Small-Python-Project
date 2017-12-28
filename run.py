import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
from app.routes import flaskrun

if __name__ == '__main__':
    flaskrun().run(
        debug=True,
        port=5000,
        host='0.0.0.0'
    )