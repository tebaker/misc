from flask import Flask
app = Flask(__name__)

# routing to the main page
@app.route('/')
def index():
    return 'index'

# routing to the a forward slash page at localhost:5000/hello
@app.route('/hello')
def hello():
    return 'Hello, World!'