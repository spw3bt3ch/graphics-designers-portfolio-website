# Professional One-Page Portfolio for Graphics Designer

A premium, modern, elegant one-page portfolio web application built with Flask, Jinja2, and Tailwind CSS. Features smooth scrolling, soft animations, and professional typography for an agency-quality design.

## ✨ Features

- **One-Page Scrolling Layout** - Smooth navigation between sections
- **Premium Design** - Modern, elegant, luxury feel with Behance-level quality
- **Responsive Design** - Mobile-first approach, works on all devices
- **Smooth Animations** - Subtle fade-in effects and hover animations
- **Professional Typography** - Google Fonts (Inter + Playfair Display)
- **Complete Sections**:
  - Hero section with CTA buttons
  - About section
  - Services showcase
  - Portfolio/Past Jobs with external links
  - Testimonials
  - Contact section
  - Footer with social links

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd OnePagePortfolio
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask application:**
   ```bash
   python app.py
   ```

6. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## 📝 Customization Guide

### 1. Social Media Links

Find and replace the following in `templates/index.html`:

#### Hero Section (around line 110):
```html
<a href="https://instagram.com/yourhandle" target="_blank" rel="noopener noreferrer" ...>
<a href="https://twitter.com/yourhandle" target="_blank" rel="noopener noreferrer" ...>
<a href="https://behance.net/yourhandle" target="_blank" rel="noopener noreferrer" ...>
<a href="https://dribbble.com/yourhandle" target="_blank" rel="noopener noreferrer" ...>
```

#### Contact Section (around line 460):
Replace the same social links in the Contact section.

#### Footer (around line 570):
Update social media links in the footer.

### 2. WhatsApp Link

Find the WhatsApp button in the Contact section (around line 485) and replace:

```html
<a href="https://wa.me/1234567890" target="_blank" ...>
```

**Format:** `https://wa.me/COUNTRYCODE+NUMBER`
- Remove any `+`, spaces, or dashes
- Example: For US number +1 (555) 123-4567, use `https://wa.me/15551234567`
- Example: For UK number +44 20 1234 5678, use `https://wa.me/442012345678`

### 3. Portfolio/Job URLs

Find the Portfolio section (around line 280) and replace:

```html
<a href="#portfolio-url-1" target="_blank" ...>
<a href="#portfolio-url-2" target="_blank" ...>
<!-- etc. -->
```

Replace `#portfolio-url-1`, `#portfolio-url-2`, etc. with your actual portfolio URLs:
- Behance project URLs
- Dribbble shot URLs
- Personal portfolio gallery URLs
- Image gallery URLs
- Any external link to showcase your work

### 4. Contact Information

Update in the Contact section (around line 440):

```html
<!-- Email -->
<p class="font-semibold text-gray-900">your.email@example.com</p>

<!-- Phone -->
<p class="font-semibold text-gray-900">+1 (555) 123-4567</p>

<!-- Location -->
<p class="font-semibold text-gray-900">New York, USA</p>
```

### 5. Personal Information

#### About Section (around line 150):
- Update the "About Me" text
- Modify skills/tags
- Replace placeholder image (currently using icon)

#### Hero Section (around line 95):
- Update the headline text
- Modify the tagline

#### Services Section (around line 200):
- Customize service descriptions
- Add/remove service cards as needed

### 6. Portfolio Projects

In the Portfolio section (around line 280):
- Update project titles
- Modify project descriptions
- Change gradient colors for each card if desired
- Add or remove portfolio cards (ensure grid stays balanced)

### 7. Testimonials

In the Testimonials section (around line 350):
- Update client names, titles, companies
- Modify testimonial text
- Add/remove testimonial cards

### 8. Meta Information

Update the page title in `<head>` (around line 6):
```html
<title>Graphics Designer Portfolio</title>
```

Add meta description for SEO (optional):
```html
<meta name="description" content="Professional graphics designer portfolio showcasing brand identity, UI/UX, and digital design work">
```

## 🎨 Design Customization

### Colors

The portfolio uses a purple-to-pink gradient theme. To change colors:

1. **Primary Gradient** - Find `gradient-bg` class in CSS (around line 45):
   ```css
   .gradient-bg {
       background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
   }
   ```

2. **Text Gradient** - Find `gradient-text` class:
   ```css
   .gradient-text {
       background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
   }
   ```

3. **Hover Colors** - Search for `hover:text-purple-600` and replace with your preferred color.

### Fonts

Current fonts: **Inter** (body) and **Playfair Display** (headings)

To change fonts:
1. Update Google Fonts link in `<head>` (around line 12)
2. Modify `font-display` class usage

### Animations

- Animation speeds are in CSS (around line 28)
- Delay classes: `delay-100`, `delay-200`, etc. (around line 35)

## 📁 Project Structure

```
OnePagePortfolio/
│
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore           # Git ignore rules
│
├── templates/
│   └── index.html       # Main portfolio template
│
└── static/              # Static files (CSS, JS, images)
    └── (add images here if needed)
```

## 🔧 Advanced Customization

### Adding Images

1. Place images in `static/` directory
2. Reference them in HTML: `{{ url_for('static', filename='image.jpg') }}`

### Adding More Sections

1. Create new section in `index.html`
2. Add navigation link in the navbar
3. Add smooth scroll anchor: `id="section-name"`
4. Update mobile menu if needed

### Form Integration

To add a contact form:
1. Install Flask-WTF: `pip install Flask-WTF`
2. Create form class in `app.py`
3. Add form HTML in Contact section
4. Handle form submission in Flask route

## 🌐 Deployment

### Deploy to Vercel (Recommended)

This project is pre-configured for Vercel deployment. See `VERCEL_DEPLOYMENT.md` for detailed instructions.

**Quick Deploy:**
1. Push your code to GitHub/GitLab/Bitbucket
2. Go to https://vercel.com/new
3. Import your repository
4. Vercel will automatically detect and deploy your Flask app

**Files included:**
- `vercel.json` - Vercel configuration
- `api/index.py` - Serverless function handler
- `.vercelignore` - Files to exclude from deployment

### Deploy to Heroku

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: gunicorn app:app
   ```
3. Add `gunicorn` to `requirements.txt`
4. Deploy: `heroku create && git push heroku main`

## 📱 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📄 License

This project is open source and available for personal and commercial use.

## 🤝 Support

For issues or questions, please check the code comments in `templates/index.html` for detailed customization instructions.

---

**Built with ❤️ using Flask + Jinja2 + Tailwind CSS**
