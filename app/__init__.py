from flask import Flask
import os

app=Flask(__name__,static_folder='static')
app.config['SECRET_KEY']='blablabla'
APP_ROOT=os.path.dirname(os.path.abspath(__file__))
app.config['DATABASE']= os.path.join(APP_ROOT, 'flaskr.sqlite')

from app import routes

from . import db
db.init_app(app)

from . import auth
app.register_blueprint(auth.bp)