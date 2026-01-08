from app import app

# Vercel serverless function handler
# This file is used by Vercel to serve the Flask app
def handler(request):
    return app(request.environ, lambda status, headers: None)
