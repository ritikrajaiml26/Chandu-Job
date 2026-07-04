# 🚀 Chandu Job Portal

A modern, highly optimized, and feature-rich Job Portal built using **Django**. This platform acts as a one-stop destination for candidates seeking government job notifications, admit cards, answer keys, exam results, admission updates, and syllabus detailed overviews.

It features a custom-designed **Premium Dark-Theme Admin Panel** with glassmorphism effects, live system telemetry, and a fully responsive, spacious data-entry layout.

---

## 🌟 Key Features

- **Job Management Module**: Create, draft, and publish job notifications with details like salary, age limits, post counts, eligibility criteria, and direct application links.
- **Results & Admit Cards Tracker**: Easy publishing and management of exam results and admit card downloads.
- **Academic Admissions**: Track university and institutional entrance notifications.
- **Syllabus & Answer Keys**: Upload and manage exam syllabi and key answer sheets.
- **Advanced Admin Panel v3.0**:
  - Full-width spacious view (removed cramped sidebar layouts).
  - Modern glassmorphism dark aesthetic (`#060514` space theme).
  - Real-time live clock & system statistics.
  - Interactive count-up metric displays.
  - Quick action buttons for high-efficiency data entry.
- **SEO & Performance Optimized**: Structured URL schema with automatic slug generation for all posts.

---

## 🛠️ Technology Stack

- **Backend Framework**: Django 6.0+
- **Database**: SQLite (Default development, easily migratable to PostgreSQL/MySQL)
- **Frontend Utilities**: HTML5, Vanilla CSS3 (custom responsive stylesheet), JavaScript, FontAwesome Icons

---

## 📂 Project Structure

```text
chandu_job/
│
├── core/                # Categories and central configurations
├── jobs/                # Job vacancy posts & detail models
├── results/             # Exam result modules
├── admitcards/          # Admit card notification modules
├── answerkeys/          # Exam answer keys
├── admissions/          # College/University admission notifications
├── syllabus/            # Detailed exam syllabi
├── accounts/            # Users, authentication, and profiles
├── pages/               # Public page views and template routing
│
├── templates/           # HTML templates (Public & Customized Admin views)
├── static/              # Compiled CSS, JS, and image assets
├── media/               # User-uploaded PDFs, images, and documents
│
├── manage.py            # Django project entrypoint
└── db.sqlite3           # SQLite Database
```

---

## 🚀 Getting Started

Follow these steps to run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/chandu-job-portal.git
cd chandu-job-portal
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
Make sure you have your requirements installed:
```bash
pip install django django-ckeditor pillow
```

### 4. Apply Database Migrations
Create the database tables and apply schema updates:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)
Generate credentials to access the custom premium Admin Control Panel:
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```
Open **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)** in your web browser and log in with your superuser credentials.

---

## 🎨 Custom Admin Theme Configurations

The custom admin overrides are located inside:
- Base site layout: `templates/admin/base_site.html`
- Dashboard metrics: `templates/admin/index.html`
- Customized job add/edit forms: `templates/admin/jobs/job/change_form.html`

Feel free to customize these stylesheets to match your branding!
