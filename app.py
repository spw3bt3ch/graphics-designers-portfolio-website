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
# This route handles static files with proper URL encoding for filenames with spaces
@app.route('/static/<path:filename>')
def serve_static(filename):
    try:
        # Decode URL-encoded filename (handles spaces and special characters like %20)
        decoded_filename = unquote(filename)
        
        # Use Flask's send_from_directory which handles path security and content types automatically
        try:
            response = send_from_directory(
                STATIC_DIR,
                decoded_filename,
                mimetype=None,
                as_attachment=False
            )
            # Add cache headers
            response.headers['Cache-Control'] = 'public, max-age=31536000'
            return response
        except (FileNotFoundError, OSError, Exception) as e:
            # If send_from_directory fails, try alternative filename matching
            # This handles case sensitivity and exact filename matching issues
            if os.path.exists(STATIC_DIR):
                available_files = os.listdir(STATIC_DIR)
                
                # Try case-insensitive matching
                for avail_file in available_files:
                    if avail_file.lower() == decoded_filename.lower() or \
                       avail_file.lower() == filename.lower() or \
                       avail_file == decoded_filename or \
                       avail_file == filename:
                        try:
                            response = send_from_directory(
                                STATIC_DIR,
                                avail_file,
                                mimetype=None,
                                as_attachment=False
                            )
                            response.headers['Cache-Control'] = 'public, max-age=31536000'
                            return response
                        except Exception as inner_e:
                            print(f"Error serving matched file '{avail_file}': {str(inner_e)}")
                            continue
                
                # If still not found, log for debugging
                print(f"Static file not found. Looking for: '{decoded_filename}' or '{filename}'")
                print(f"Available files in static directory: {available_files}")
                abort(404)
            else:
                print(f"Static directory does not exist: {STATIC_DIR}")
                abort(404)
    except Exception as e:
        print(f"Error serving static file '{filename}': {str(e)}")
        import traceback
        traceback.print_exc()
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
