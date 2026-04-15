"""GRUT RAI v2 — Dashboard Server"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, send_from_directory
from ui.api.routes import api

app = Flask(__name__, static_folder='static')
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
