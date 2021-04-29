

import argparse
import model.train_model
import tensorflow as tf

print(tf.__version__)

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to input dataset")
ap.add_argument("-p", "--plot", type=str, default='plot.png', help="path to output loss/accuracy plot")
ap.add_argument("-m", "--model", type=str, default="pneumonia.model", help='model name')
args = vars(ap.parse_args())

INIT_LR = 1e-3
EPOCHS = 25
BS = 8

saved_model = tf.keras.models.load_model(args['model'])

if not saved_model:
    model.train_model.train_model(args, INIT_LR, EPOCHS, BS)
else:
    print('Model Loaded')



