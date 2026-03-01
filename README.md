<div align="center">

# 🚀 Flask User Management Application

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

A simple yet elegant Flask web application to **view**, **add**, and **look up** user details.  
Data is stored in an **SQLite** database — no MySQL installation required!

[View Demo](#running-the-application) · [Report Bug](../../issues) · [Request Feature](../../issues)

</div>

---

## 📑 Table of Contents

<details>
<summary>Click to expand</summary>

- [Prerequisites](#-prerequisites)
- [Setup & Installation](#-setup--installation)
- [Running the Application](#-running-the-application)
- [Deployment (Render)](#-deployment-render)
- [Application Routes](#-application-routes)
- [Database Schema](#-database-schema)
- [SQL Queries (Task 2)](#-sql-queries-task-2)
- [Git Workflow (Task 3)](#-git-workflow-task-3)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [Additional Notes](#-additional-notes)

</details>

---

## ✅ Prerequisites

| Requirement | Version | Link |
|:-----------:|:-------:|:----:|
| Python | 3.x | [Download](https://www.python.org/downloads/) |
| pip | (bundled with Python) | — |
| Git | Latest | [Download](https://git-scm.com/downloads) |

> [!NOTE]
> This project uses **SQLite** (built into Python) instead of MySQL, so you do **not** need to install any database server.

---

## 🛠 Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/david-one8/Assignment-SDE.git
cd Assignment-SDE
```

**2. Create a virtual environment _(optional but recommended)_**
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS / Linux:
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the application**
```bash
python app.py
```

> [!TIP]
> The database (`users.db`) is **automatically created** with 5 sample users when you start the app for the first time. No need to run `init_db.py` manually!

---

## ▶️ Running the Application

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000/
```

🎉 **That's it — the app is running!**

---

## ☁️ Deployment (Render)

This app is configured for easy deployment on [Render](https://render.com).

### Deploy to Render

1. Push your code to GitHub
2. Go to [render.com](https://render.com) and create a new **Web Service**
3. Connect your GitHub repository
4. Configure the service:

| Setting | Value |
|:--------|:------|
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Environment** | Python 3 |

5. Click **Deploy**

> [!NOTE]
> The database auto-initializes on startup. However, Render's free tier has **ephemeral storage** — data added at runtime may be lost on restart. For persistent data, consider using Render's PostgreSQL.

### Live Demo

🔗 **[https://assignment-sde.onrender.com](https://assignment-sde.onrender.com)**

---

## 🌐 Application Routes

| Route | Method | Description |
|:------|:------:|:------------|
| `/hello` | `GET` | Returns the **"Hello World!"** greeting page |
| `/users` | `GET` | Displays all users in an HTML table |
| `/users/<id>` | `GET` | Shows details for a specific user |
| `/new_user` | `GET` | Renders a form to add a new user |
| `/new_user` | `POST` | Validates & stores the new user in the database |

> [!TIP]
> A custom **404 error page** is shown whenever a user or resource is not found.

---

## 🗄 Database Schema

**Database file:** `users.db` (SQLite)

### Table: `users`

| Column | Type | Constraints |
|:------:|:----:|:------------|
| `id` | `INTEGER` | `PRIMARY KEY`, `AUTOINCREMENT` |
| `name` | `VARCHAR(100)` | `NOT NULL` |
| `email` | `VARCHAR(100)` | `NOT NULL` |
| `role` | `VARCHAR(50)` | `NOT NULL` |

### Populating Sample Data

```bash
python init_db.py
```

This inserts **5 sample users** (Alice, Bob, Charlie, Diana, Eve) into the database.

---

## 📝 SQL Queries (Task 2)

<details>
<summary><b>a) Create the <code>users</code> table</b></summary>

```sql
CREATE TABLE IF NOT EXISTS users (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    role  VARCHAR(50)  NOT NULL
);
```

</details>

<details>
<summary><b>b) Insert sample data</b></summary>

```sql
INSERT INTO users (name, email, role) VALUES ('Alice Johnson', 'alice@example.com', 'Developer');
INSERT INTO users (name, email, role) VALUES ('Bob Smith',     'bob@example.com',   'Designer');
INSERT INTO users (name, email, role) VALUES ('Charlie Brown', 'charlie@example.com','Manager');
INSERT INTO users (name, email, role) VALUES ('Diana Prince',  'diana@example.com', 'Developer');
INSERT INTO users (name, email, role) VALUES ('Eve Davis',     'eve@example.com',   'Tester');
```

</details>

<details>
<summary><b>c) Retrieve all users</b></summary>

```sql
SELECT * FROM users;
```

</details>

<details>
<summary><b>d) Retrieve a specific user by ID</b></summary>

```sql
SELECT * FROM users WHERE id = 1;
```

</details>

---

## 🔀 Git Workflow (Task 3)

### Branch Strategy

```
main ─────────────────────────────────── (base branch)
  \
   └── assignment ── commit1 ── commit2 ── ... ── commitN ── PR → main
```

### Initial Setup

```bash
# Initialize a git repo
git init

# Create and switch to the "assignment" branch
git checkout -b assignment

# Stage and commit your work
git add .
git commit -m "Initial commit: Flask app with user management"

# Add remote and push
git remote add origin https://github.com/david-one8/Assignment-SDE.git
git push -u origin assignment
```

### Creating a Pull Request

1. Go to your GitHub repository in a browser
2. Click the **"Compare & pull request"** banner (or go to **Pull Requests → New**)
3. Set **base:** `main` ← **compare:** `assignment`
4. Add a title & description, then click **"Create pull request"**

---

## 📁 Project Structure

```
Assignment-SDE/
│
├── 📄 app.py               # Main Flask application (routes & logic)
├── 📄 init_db.py            # Database initialization script
├── 📄 sql_queries.py        # SQL queries reference (Task 2)
├── 📄 requirements.txt      # Python dependencies
├── 📄 .gitignore            # Git ignore rules
├── 📄 README.md             # This file
│
└── 📂 templates/
    ├── base.html            # Base layout with Bootstrap 5 & navbar
    ├── hello.html           # Hello World greeting page
    ├── users.html           # All users displayed in a table
    ├── user_detail.html     # Individual user details card
    ├── new_user.html        # New user creation form
    └── 404.html             # Custom error page
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit** your changes
   ```bash
   git commit -m "Add amazing feature"
   ```
4. **Push** to your branch
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open** a Pull Request against `main`

---

## 📌 Additional Notes

| Topic | Details |
|:------|:--------|
| **SQLite vs MySQL** | This project uses SQLite for zero-install simplicity. To switch to MySQL, install `mysql-connector-python`, update `get_db_connection()` in `app.py`, and change `?` placeholders to `%s`. |
| **Styling** | Bootstrap 5 is loaded via CDN — no local CSS files needed. |
| **Auto-Init Database** | The app automatically creates the database and sample users on first run — no manual setup needed. |
| **Production Server** | Uses `gunicorn` for production deployment. Locally, Flask's dev server is used. |
| **Debug Mode** | Disabled in production. Set `debug=True` in `app.py` for local development if needed. |

---

<div align="center">

**Made with ❤️ using Flask & Python**

</div>
