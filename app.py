from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='build', static_url_path='/')

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello from Flask!")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    return send_from_directory(app.static_folder, path) if path else send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=False)  
