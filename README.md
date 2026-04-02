# My django website

THIS REPO IS FOR MY PERSONAL USE, AND THIS READ ME IS MEANT FOR ME TO REMEMBER WHAT I MADE HERE.

This repository contains a Django-powered Content Management Systems designed to export as a static website for hosting on GitHub Pages (mariobx.github.io).

## Technical Architecture

*   **Framework**: Django 6.0.3 (Python 3.14)
*   **Static Export**: `django-distill`
*   **Media Processing**: `yt-dlp` for YouTube ID extraction and `Pillow` for images.
*   **Database**: SQLite (db.sqlite3 is tracked in Git to serve as the CMS state).
*   **Deployment**: GitHub Actions (Automatic distilling of Django into static HTML).

---

## Local Management Workflow

### 1. Development
Run the local server to manage content:
```bash
./venv/bin/python manage.py runserver
```

### 2. Managing Content (The Admin)
Access the dashboard at `http://127.0.0.1:8000/admin/`.
*   **Home Page**: Edit your name and bio text.
*   **Projects**: Add project details, source links, and tech stacks.
*   **Project Media**: Upload GIFs/Images OR paste YouTube links.
    *   *Mutual Exclusivity*: Each media item must be either a file or a link, not both.
    *   *YouTube Logic*: If an embed is blocked by copyright, check the `Blocked embed` box to show a fallback thumbnail + play button.
*   **Resumes**: Upload PDFs and set their slug (e.g., `gov_resume`).

### 3. Database & Migrations
The database schema is locked into `0001_initial.py`. If you modify models, you must run migrations and push the new migration file to GitHub.

---

## Deployment Workflow

### Step 1: Push Source
Stage and push your changes (including `db.sqlite3` and any new files in `media/`) to this repository.
```bash
git add .
git commit -m "Update project content"
git push origin main
```

### Step 2: Trigger GitHub Action
1.  Go to the **Actions** tab in this GitHub repository.
2.  Select **"Deploy Static Site"** from the sidebar.
3.  Click **"Run workflow"**.

### What the Action Does:
1.  Checkouts the source code.
2.  Sets up Python and installs dependencies.
3.  Runs `collectstatic` to gather assets.
4.  Runs `distill-local` to create the site into an `output/` folder.
5.  Pushes the contents of `output/` directly to the `mariobx/mariobx.github.io` repository.

---

## Security & Settings

*   **Secret Key**: Loaded from `config/.secret`. This file is ignored by Git. The GitHub Action uses a placeholder key for the build process.
*   **Referrer Policy**: Set to `strict-origin-when-cross-origin` in `settings.py` to allow YouTube embeds to verify the domain.
*   **X-Frame-Options**: Set to `SAMEORIGIN` to support embedded previews.
*   **Analytics**: Google Analytics (gtag.js) is hardcoded into the `base.html` header.

---

## Media Constraints
*   **File Size**: GitHub rejects files over 100MB. Compress large GIFs using `gifsicle` before uploading.
*   **Static Assets**: All PDFs should be stored in `static/pdf/` and registered in the Admin.
