from app import APP_ROOT
import tensorflow as tf
import os
import numpy as np
import cv2

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
static_loc=os.path.join(APP_ROOT,'static/')

def load_model(model_path="pneumonia.model"):
    loaded_model = tf.keras.models.load_model(model_path)
    return loaded_model

def prepare_image(img_path):
    data = []
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    data.append(image)
    data = np.array(data) / 255.0
    return data

def predict_img(filename):
    classes = ['Normal', 'Pneumonia']
    target=os.path.join(APP_ROOT,'temp/'+filename)
    model = load_model()
    image = prepare_image(target)
    prediction = model.predict(image)
    return classes[np.argmax(prediction[0])]