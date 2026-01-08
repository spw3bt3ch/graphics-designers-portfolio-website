# Vercel Deployment Guide

This Flask application is configured for deployment on Vercel.

## Prerequisites

1. A Vercel account (sign up at https://vercel.com)
2. Vercel CLI installed (optional, for CLI deployment)

## Deployment Steps

### Option 1: Deploy via Vercel Dashboard

1. **Push your code to GitHub/GitLab/Bitbucket**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Import Project on Vercel**
   - Go to https://vercel.com/new
   - Import your Git repository
   - Vercel will automatically detect the Python/Flask project

3. **Configure Build Settings**
   - Framework Preset: Other
   - Build Command: (leave empty or use `pip install -r requirements.txt`)
   - Output Directory: (leave empty)
   - Install Command: `pip install -r requirements.txt`

4. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```

4. **For Production Deployment**
   ```bash
   vercel --prod
   ```

## Configuration Files

- `vercel.json` - Vercel configuration for Python/Flask
- `api/index.py` - Serverless function handler (if needed)
- `requirements.txt` - Python dependencies

## Important Notes

1. **Static Files**: All static files (images, CSS, JS) should be in the `static/` directory. Vercel will serve them automatically.

2. **Environment Variables**: If you need environment variables:
   - Go to Vercel Dashboard → Your Project → Settings → Environment Variables
   - Add your variables there

3. **Build Settings**: Vercel automatically detects Python projects and uses the `@vercel/python` builder.

4. **Custom Domain**: After deployment, you can add a custom domain in the Vercel dashboard.

## Troubleshooting

### If deployment fails:

1. Check that all dependencies are in `requirements.txt`
2. Ensure `app.py` is in the root directory
3. Verify that `templates/` and `static/` directories exist
4. Check Vercel build logs for specific errors

### Common Issues:

- **Module not found**: Add missing packages to `requirements.txt`
- **Template not found**: Ensure `templates/` directory is in the root
- **Static files not loading**: Check that files are in `static/` directory

## Post-Deployment

After successful deployment:
1. Your app will be available at `https://your-project.vercel.app`
2. You can view deployment logs in the Vercel dashboard
3. Each git push will trigger a new deployment automatically

## Support

For Vercel-specific issues, check:
- Vercel Documentation: https://vercel.com/docs
- Python Runtime: https://vercel.com/docs/runtimes/python
