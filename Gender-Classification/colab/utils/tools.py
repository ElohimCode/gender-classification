import cv2
import tensorflow as tf
import numpy as np


def load_img(path):
    image = tf.image.resize(cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB), (256, 256))
    return np.expand_dims(image/255, 0)
