from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h>Hello, World!</h>'



# pip install flask
# flask run --port 8000