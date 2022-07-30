# python 3.8

from flask import Flask

app = Flask(__name__)

@app.route("/hw")
def hello_world():
    return "<p><b>Hello, world!</b></p>"