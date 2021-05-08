from flask import render_template, request, redirect, flash

from app import app,APP_ROOT
from app.process import predict_img
import os
from app.db import get_db


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
        file = request.files['imgInp']
        filename = file.filename
        file.save("".join([target, filename]))
        print("Upload Complete")
        return redirect('/prediction/{}'.format(filename))

@app.route("/prediction/<filename>",methods=["GET", "POST"])
def prediction(filename):
    db = get_db()
    fileResult = db.execute(
        'SELECT * FROM xray_results WHERE xray_name = ?', (filename,)
    ).fetchone()

    if fileResult is None:
        x = predict_img(filename)
        db.execute(
            'INSERT INTO xray_results (xray_name, result) VALUES (?, ?)', (filename, x,)
        )
    else:
        x = fileResult['result']
        flash("Retrieved from DB")

    return render_template('output.html', results=x)