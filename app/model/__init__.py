
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# imports 
import tensorflow.keras as keras
import tensorflow as tf
import numpy as np
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array


def normalize_image(image):
    image = image / 255.0 # with the format we used on the train data.
    return image

def prepare_image(image, target):
    # if the image is not RGB then convert it to RGB
    if image.mode != "RGB":
        image = image.convert("RGB")
    # resize the image to desired shape
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = normalize_image(image)
    return image


# classes
classes = {0: 'female', 1: 'male'}

# model name
MODEL_NAME = "gender-classification.h5"

MODEL_PATH = os.path.join(os.getcwd(), "static", MODEL_NAME)

print(" * LOADING MODEL")
model = keras.models.load_model(MODEL_PATH)
print("\n * MODEL LOADED SUCCESSFULLY\n")


def make_prediction(model, image):
  preds = model(image)
  predictions = tf.squeeze(preds).numpy()
  prediction = np.argmax(predictions).astype("int32")
  preds_list = [{
      "label": int(i),
      "class": classes[i],
      "probability": float(np.round(pred, 2))
  } for i, pred in enumerate(predictions)]
  
  meta ={
      "programmer": "@crispengari",
      "main": "computer vision (cv)",
      "description": "classifying gender based on the face of a human being, (vgg16).",
      "language": "python",
      "library": "tensforflow: v2.*"
  }
  return {
      "meta":meta,
      "label": int(prediction),
      "class": classes[prediction],
      "probability": float(np.round(predictions[prediction], 2)),
      "predictions": preds_list
  }


