# My Portfolio Website

**A comprehensive showcase of all my work, projects, and professional experience.**

This is a personal portfolio website built with Flask that displays my complete body of work, skills, and provides a way for visitors to get in touch with me.

## Features

- **Home Page** - Introduction and overview
- **About** - Background and professional information
- **Works** - Complete gallery showcasing ALL of my projects and accomplishments
- **Contact** - Form for visitors to reach out (submissions saved to CSV/text files)
- **Thank You** - Confirmation page after contact form submission

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML/CSS
- **Data Storage**: CSV and text files for contact form submissions

## Project Structure

```
portfolio/
├── server.py           # Flask application and routes
├── templates/          # HTML templates
│   ├── index.html     # Home page
│   ├── about.html     # About page
│   ├── works.html     # Portfolio showcase
│   ├── contact.html   # Contact form
│   └── thankyou.html  # Thank you page
├── static/            # CSS, images, and other assets
├── database.csv       # Contact form submissions (CSV)
└── database.txt       # Contact form submissions (text)
```

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install flask
   ```

## Running the Application

```bash
python server.py
```

Then open your browser and navigate to `http://localhost:5000`

## Contact Form

The contact form allows visitors to send messages, which are automatically saved to both:
- `database.csv` - Structured CSV format
- `database.txt` - Plain text format

---

**This portfolio represents the complete collection of my work and achievements.**
