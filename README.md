# Toh Tech Flask

A small Flask web project I'm building to practice web development — user registration, SQLAlchemy database models, and a protected admin page to view registered users in a table.

This is a personal learning/practice project, so the structure and features will keep evolving as I learn.

## Screenshot

![./screenshots/flask_coding_illustration.png]



## Features

- User registration form (stores data via SQLAlchemy + SQLite)
- Passwords are hashed with `werkzeug.security` before being stored
- Admin-only page (`/admin/users`) to view all registered users in a table
- Simple session-based login to protect the admin page
- Pages: Home, Welcome, About, Visit, Registration

## Built With

- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- SQLite
- Jinja2 templates

## Running Locally

```bash
# activate your virtual environment first, then:
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

## 📂 Project Structure

```
Toh tech Flask/
├── app.py
├── templates/
│   ├── home.html
│   ├── welcome.html
│   ├── about.html
│   ├── visit.html
│   ├── register.html
│   └── users.html
├── screenshots/
│   └── homepage.png
└── README.md
```

## Notes

This project is a work in progress, built for practicing:
- Flask routing
- SQLAlchemy models and queries
- Jinja2 templating
- Basic auth/session handling

---
