from flask import abort, Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello world!"