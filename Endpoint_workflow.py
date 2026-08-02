from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the App"

@app.route('/health')
def health():
    return "App is running"


