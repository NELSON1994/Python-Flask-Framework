from flask import Flask, redirect, url_for

app = Flask(__name__)

from app import routes
