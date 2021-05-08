import argparse
import model.train_model
import tensorflow as tf
import os
import matplotlib.pyplot as plt

'''
Brian Oliver
Western Governors University
'''

def createFileList(myDir, format='.jpeg'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList

def refresh():
    print("Refreshing visualizations")

    plt.style.use('ggplot')
    labels = ['NORMAL', 'PNEUMONIA']
    normal_count = len([name for name in os.listdir('./dataset/NORMAL')])
    pneumonia_count = len([name for name in os.listdir('./dataset/PNEUMONIA')])
    counts = [normal_count, pneumonia_count]
    x_pos = [i for i, _ in enumerate(labels)]
    plt.bar(x_pos, counts, color='green')
    plt.xlabel('Diagnosis')
    plt.ylabel('Frequency')
    plt.title('Frequency of Chest X-ray Types in Testing Set')

    plt.xticks(x_pos, labels)

    plt.show()

    plt.show()



# Prints the tensorflow version for troubleshooting.
print(tf.__version__)

# Arguments needed for setting up the pneumonia.model on first run.
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to input dataset")
ap.add_argument("-p", "--plot", type=str, default='plot.png', help="path to output loss/accuracy plot")
ap.add_argument("-m", "--model", type=str, default="pneumonia.model", help='model name')
ap.add_argument("-rf", "--refresh", type=str, default="FALSE", help='pass TRUE to refresh graphs/visualizations')
args = vars(ap.parse_args())

# Arguments needed to fine-tune ML training.
INIT_LR = 1e-3
EPOCHS = 25
BS = 8

# Loads the model if one exists.
saved_model = tf.keras.models.load_model(args['model'])

# Trains a new model if one does not exist.
if not saved_model:
    model.train_model.train_model(args, INIT_LR, EPOCHS, BS)
else:
    print('Model Loaded')

# Data Visualization
if args['refresh'] == "TRUE":
    refresh()
