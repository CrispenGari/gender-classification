from flask import Blueprint, make_response, jsonify, request
from PIL import Image
from model import make_prediction, model, prepare_image
import io

blueprint = Blueprint("blueprint",__name__)

@blueprint.route('/gender', methods=["POST"])
def classify_gender():
    data = {"success": False}
    if request.method == "POST":
        if request.files.get("image"):
            # read the image in PIL format
            image = request.files.get("image").read()
            image = Image.open(io.BytesIO(image))

            # preprocess the image
            image = prepare_image(image, target=(96, 96))
            preds = make_prediction(model, image)
            
            data["success"] = True
            data["predictions"] = preds
            print(preds)      
    return make_response(jsonify(data)), 200