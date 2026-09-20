from flask import Flask, send_from_directory
import os

app = Flask(__name__)

BASE = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(BASE, 'web')
TUNES_DIR = os.path.join(BASE, 'tunes')

@app.route('/')
def index():
    return send_from_directory(WEB_DIR, 'index.html')

@app.route('/tunes/<path:filename>')
def tunes(filename):
    return send_from_directory(TUNES_DIR, filename)

if __name__ == '__main__':
    print("Pyano web app running at http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
