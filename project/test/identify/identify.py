from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import os

tf.get_logger().setLevel('ERROR')

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppresses all logs below ERROR level
model = load_model(os.path.join(os.getcwd(), 'test\identify\model.h5'))

classes = ['dog','horse','elephant','butterfly', 'chicken', 'housecat', 'cow','sheep', 'spider', 'squirrel']

def identify(path):

    input = image.load_img(path, target_size=(224, 224))
    input = image.img_to_array(input)
    input = np.array([input])
    input = preprocess_input(input)

    pred = model.predict(input)
    predInd = np.argmax(pred)

    return classes[predInd]
