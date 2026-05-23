# EduNex University Management System

Complete university management system with 3 portals:
- Indigene Verification Portal
- Admission / E-Screening Portal  
- Student Portal

## Quick Deploy (Render)

1. Fork/push this repo to GitHub
2. Create [Neon](https://neon.tech) PostgreSQL database (free tier)
3. Create [Cloudinary](https://cloudinary.com) account (free tier)
4. Sign up on [Render](https://render.com)
5. New Web Service -> Connect GitHub repo
6. Add environment variables in Render dashboard
7. Deploy

## PythonAnywhere Deploy

1. Upload files or clone from GitHub
2. Create virtualenv: mkvirtualenv --python=python3.11 edunex
3. Install: pip install -r requirements.txt
4. In Web tab: set WSGI to config.wsgi
5. Set static files path
6. Run migrations in console
7. Reload web app

## Setup Wizard

First visit will redirect to /setup/ to configure university.
