import os
import tensorflow as tf
from tensorflow.keras.models import load_model

from .CONSTANTS import classes, THRESHOLD

def get_class(result):
    val = result[0][0]
    data = {
        "class":  "",
        "accuracy": ""
    }

    if val > THRESHOLD:
        val = val*100
        data["class"], data["accuracy"] = classes[1], val
        
        return data
    
    else:
        val = (1-val)*100
        data["class"], data["accuracy"] = classes[0], val
        return data


def predicts(model_path, img):
    try:        
        model = load_model(model_path)
    except OSError as err:
        model = model_path
    finally:
        result = model.predict(img)
        return get_class(result=result)


