from app import app

# Vercel serverless function handler
# Vercel Python runtime expects a WSGI application
# Export the Flask app directly as it's WSGI-compatible
application = app

# Handler function for Vercel serverless functions
# This is called by Vercel's Python runtime
def handler(request, start_response):
    """
    Vercel WSGI handler
    request: werkzeug.wrappers.Request object
    start_response: WSGI start_response callable
    """
    return app(request.environ, start_response)
