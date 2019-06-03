from flask import Flask
from cicd.main import practice
app = Flask(__name__)


@app.route('/practice')
def get_practice():
    return str(practice())