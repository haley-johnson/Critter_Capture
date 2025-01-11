from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

tf.get_logger().setLevel('ERROR')

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppresses all logs below ERROR level

classes = ['dog','horse','elephant','butterfly', 'chicken', 'housecat', 'cow','sheep', 'spider', 'squirrel']

def identify(path):
    model = load_model('identify/model.h5')

    input = image.load_img(path, target_size=(224, 224))
    input = image.img_to_array(input)
    input = np.array([input])
    input = preprocess_input(input)

    pred = model.predict(input)
    predInd = np.argmax(pred)

    return classes[predInd]
