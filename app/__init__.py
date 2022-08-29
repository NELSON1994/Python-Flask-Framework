from flask import Flask, redirect, url_for

app = Flask(__name__)

from app import routes
#
# app.config.from_object(Config)
#
# print("APP SECRET KEY : ", config.Config.SECRET_KEY)
