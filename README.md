# Flask User Management Application

A simple Flask web application that allows you to manage users — **view**, **add**, and **look up** user details. Data is stored in an **SQLite** database (no MySQL installation required).

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup & Installation](#setup--installation)
3. [Running the Application](#running-the-application)
4. [Application Routes](#application-routes)
5. [Database Schema](#database-schema)
6. [SQL Queries (Task 2)](#sql-queries-task-2)
7. [Git Workflow (Task 3)](#git-workflow-task-3)
8. [Project Structure](#project-structure)
9. [Contributing](#contributing)

---

## Prerequisites

- **Python 3.x** — [Download here](https://www.python.org/downloads/)
- **pip** — comes pre-installed with Python 3.x
- **Git** — [Download here](https://git-scm.com/downloads)

> **Note:** This project uses **SQLite** (built into Python) instead of MySQL, so you do **not** need to install any database server.

---

## Setup & Installation

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd eactive-assignment

# 2. (Optional) Create a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize the database with sample data
python init_db.py
```

After step 4 you will see a file called `users.db` — this is the SQLite database.

---

## Running the Application

```bash
python app.py
```

The development server starts at **http://127.0.0.1:5000/**. Open this URL in your browser.

---

## Application Routes

| Route | Method | Description |
|---|---|---|
| `/hello` | GET | Returns **"Hello World!"** greeting page |
| `/users` | GET | Displays all users in an HTML table |
| `/users/<id>` | GET | Shows details for a specific user |
| `/new_user` | GET | Renders a form to add a new user |
| `/new_user` | POST | Submits the form and stores the user in the database |

- A **404 error page** is shown when a user or resource is not found.

---

## Database Schema

**Database name:** `users.db` (SQLite file)

**Table: `users`**

| Column | Type | Constraints |
|---|---|---|
| `id` | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| `name` | VARCHAR(100) | NOT NULL |
| `email` | VARCHAR(100) | NOT NULL |
| `role` | VARCHAR(50) | NOT NULL |

### Populating Sample Data

Run the initialization script once:

```bash
python init_db.py
```

This inserts 5 sample users into the database.

---

## SQL Queries (Task 2)

### a) Create the `users` table

```sql
CREATE TABLE IF NOT EXISTS users (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    role  VARCHAR(50)  NOT NULL
);
```

### b) Insert sample data

```sql
INSERT INTO users (name, email, role) VALUES ('Alice Johnson', 'alice@example.com', 'Developer');
INSERT INTO users (name, email, role) VALUES ('Bob Smith',     'bob@example.com',   'Designer');
INSERT INTO users (name, email, role) VALUES ('Charlie Brown', 'charlie@example.com','Manager');
INSERT INTO users (name, email, role) VALUES ('Diana Prince',  'diana@example.com', 'Developer');
INSERT INTO users (name, email, role) VALUES ('Eve Davis',     'eve@example.com',   'Tester');
```

### c) Retrieve all users

```sql
SELECT * FROM users;
```

### d) Retrieve a specific user by ID

```sql
SELECT * FROM users WHERE id = 1;
```

---

## Git Workflow (Task 3)

### Initial Setup

```bash
# Initialize a git repo
git init

# Create and switch to the "assignment" branch
git checkout -b assignment

# Add all files and make the initial commit
git add .
git commit -m "Initial commit: Flask app with user management"

# Add your remote repository
git remote add origin <your-repo-url>

# Push the branch
git push -u origin assignment
```

### Creating a Pull Request

1. Go to your GitHub / GitLab repository in a browser.
2. You will see a prompt to create a **Pull Request** from `assignment` → `main`.
3. Click **"Compare & pull request"**.
4. Add a title and description, then click **"Create pull request"**.

### Contributing

1. Fork or clone the repository.
2. Create a new feature branch: `git checkout -b feature/your-feature`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature`
5. Open a Pull Request against the `main` branch.

---

## Project Structure

```
eactive-assignment/
├── app.py              # Main Flask application
├── init_db.py          # Database initialization script
├── sql_queries.py      # SQL queries reference (Task 2)
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── templates/
    ├── base.html       # Base layout (Bootstrap 5)
    ├── hello.html      # Hello World page
    ├── users.html      # All users table
    ├── user_detail.html# Single user details
    ├── new_user.html   # Add new user form
    └── 404.html        # Error page
```

---

## Additional Notes

- **SQLite vs MySQL:** This project uses SQLite for simplicity (zero installation). To switch to MySQL, install `mysql-connector-python`, update the `get_db_connection()` function in `app.py`, and change `?` placeholders to `%s`.
- **Bootstrap 5** is loaded via CDN for styling — no local CSS files needed.
- **Debug mode** is enabled by default (`app.run(debug=True)`). Disable it in production.
