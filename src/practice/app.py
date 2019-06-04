from flask import Flask, request
app = Flask(__name__)

@app.route("/practice")
def practice():
    return "Hello world!"