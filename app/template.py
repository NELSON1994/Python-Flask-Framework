from flask import Flask, redirect, url_for, request, render_template
from app import app

app = Flask(__name__)


@app.route('/hello/<user>/<department>')
def hello_name(user, department):
    return render_template('hello.html', name=user, department=department)
