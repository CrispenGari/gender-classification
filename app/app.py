from api import app
from flask import make_response, jsonify
from blueprints import blueprint
app.register_blueprint(blueprint, url_prefix="/api")

class AppConfig:
    PORT = 3001
    DEBUG = False
    
    
@app.route('/', methods=["GET"])
def meta():
    meta ={
        "programmer": "@crispengari",
        "main": "computer vision (cv)",
        "description": "classifying gender based on the face of a human being, (vgg16).",
        "language": "python",
        "library": "tensforflow: v2.*"
    }
    return make_response(jsonify(meta)), 200

if __name__ == "__main__":
    app.run(debug=AppConfig().DEBUG, port=AppConfig().PORT, )