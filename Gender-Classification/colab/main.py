import os

from utils.tools import load_img
from utils.prediction import predicts

img = load_img(path='C:/Users/JB/Pictures/Camera Roll/WIN_20230502_03_19_12_Pro.jpg')


if __name__ == '__main__':
    result = predicts(model_path=os.path.join('models', 'imageclassifier.h5'), img=img)
    print(result)
