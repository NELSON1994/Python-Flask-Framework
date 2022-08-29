from flask import Flask, redirect, url_for
from flask_mail import Mail

app = Flask(__name__)

from app import routes

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
#
# app.config.from_object(Config)
#
# print("APP SECRET KEY : ", config.Config.SECRET_KEY)
