from flask import Flask, render_template, request, jsonify
from main import generate_path
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def get_path():
    topic = request.args.get('topic', '')
    if not topic:
        return jsonify({"error": "No topic provided"}), 400
    return jsonify(generate_path(topic))

# DO NOT include app.run() here for Vercel
