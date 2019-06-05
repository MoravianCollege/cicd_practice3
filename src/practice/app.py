from flask import Flask
from practice.main import hello
app = Flask(__name__)


@app.route('/hello')
def get_hello():
    return str(hello())