from flask import Flask, render_template, send_from_directory, request, abort, Response
import os
from urllib.parse import unquote

# Get the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

app = Flask(__name__, static_folder=STATIC_DIR, static_url_path='/static')
app.config['SECRET_KEY'] = 'your-secret-key-here'

@app.route('/')
def index():
    return render_template('index.html')

# Serve static files explicitly for Vercel
@app.route('/static/<path:filename>')
def serve_static(filename):
    try:
        # Decode URL-encoded filename (handles spaces and special characters like %20)
        decoded_filename = unquote(filename)
        
        # Try multiple approaches to find the file
        # First, try with decoded filename
        file_path = os.path.join(STATIC_DIR, decoded_filename)
        file_path = os.path.normpath(file_path)
        
        # Ensure the file is within the static directory
        static_dir_norm = os.path.normpath(STATIC_DIR)
        if not file_path.startswith(static_dir_norm):
            abort(404)
        
        # If file doesn't exist with decoded name, try with original encoded name
        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            # Try with original filename
            alt_path = os.path.join(STATIC_DIR, filename)
            alt_path = os.path.normpath(alt_path)
            if alt_path.startswith(static_dir_norm) and (os.path.exists(alt_path) and os.path.isfile(alt_path)):
                file_path = alt_path
                decoded_filename = filename
            else:
                # List available files for debugging (remove in production)
                if os.path.exists(STATIC_DIR):
                    available_files = os.listdir(STATIC_DIR)
                    print(f"Looking for: {decoded_filename}")
                    print(f"Available files: {available_files}")
                abort(404)
        
        # Determine content type
        content_type = 'application/octet-stream'
        if decoded_filename.lower().endswith(('.jpg', '.jpeg')):
            content_type = 'image/jpeg'
        elif decoded_filename.lower().endswith('.png'):
            content_type = 'image/png'
        elif decoded_filename.lower().endswith('.gif'):
            content_type = 'image/gif'
        elif decoded_filename.lower().endswith('.webp'):
            content_type = 'image/webp'
        
        # Read and send the file
        with open(file_path, 'rb') as f:
            file_data = f.read()
        
        return Response(
            file_data,
            mimetype=content_type,
            headers={
                'Cache-Control': 'public, max-age=31536000'
            }
        )
    except Exception as e:
        print(f"Error serving static file: {str(e)}")
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
