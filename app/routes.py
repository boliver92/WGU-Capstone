from flask import render_template, request, redirect

from app import app,APP_ROOT
from app.process import predict_img
import os


@app.route('/')
def home():
    return render_template('predict.html',title='Home')

@app.route('/about')
def about():
    return render_template('about.html',title='About',name='Passed by variable')

@app.route('/predict')
def predict():
    return render_template("predict.html", title="Predict")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    target = os.path.join(APP_ROOT, 'temp\\')
    if request.method == "POST":
        file = request.files['img']
        filename = file.filename
        file.save("".join([target, filename]))
        print("Upload Complete")
        return redirect('/prediction/{}'.format(filename))

@app.route("/prediction/<filename>",methods=["GET", "POST"])
def prediction(filename):
    x = predict_img(filename)
    return render_template('output.html', results=x)