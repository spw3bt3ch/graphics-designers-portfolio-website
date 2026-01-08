from app import app

# Vercel serverless function handler
# Vercel Python runtime expects a WSGI application
# Export the Flask app directly as it's WSGI-compatible
# This is the standard pattern for Flask apps on Vercel
application = app
