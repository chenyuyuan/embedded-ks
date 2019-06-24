from flask import Flask
from flask import render_template

import RPi.GPIO as GPIO
import time


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("control.html")

@app.route('/he')
def hello_world():
    return 'Hello World!'

@app.route('/rgb_led')
def rgb_led():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
