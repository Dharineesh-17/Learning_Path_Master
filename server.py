from flask import Flask, render_template, request, jsonify
from main import generate_path

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/generate')
def get_path():
    topic = request.args.get('topic', '')
    if not topic:
        return jsonify({"error": "No topic provided"}), 400
    # Calls the AI logic in main.py
    return jsonify(generate_path(topic))

if __name__ == '__main__':
    app.run(debug=True, port=5000)