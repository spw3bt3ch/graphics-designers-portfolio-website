from flask import Flask, render_template, send_from_directory, request
import os
from urllib.parse import unquote

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SECRET_KEY'] = 'your-secret-key-here'

@app.route('/')
def index():
    return render_template('index.html')

# Serve static files explicitly for Vercel
@app.route('/static/<path:filename>')
def serve_static(filename):
    # Decode URL-encoded filename (handles spaces and special characters)
    filename = unquote(filename)
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
