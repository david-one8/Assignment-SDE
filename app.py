"""
Flask Application - User Management System
This application provides routes to manage users stored in a SQLite database.
"""

import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

# Database helper
DATABASE = "users.db"


def get_db_connection():
    """Create and return a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # So we can access columns by name
    return conn


# Routes


@app.route("/")
def index():
    """Home page – redirects to /hello."""
    return redirect(url_for("hello"))


@app.route("/hello")
def hello():
    """Return 'Hello World!' greeting page."""
    return render_template("hello.html")


@app.route("/users")
def users():
    """Retrieve all users from the database and display them in an HTML table."""
    conn = get_db_connection()
    all_users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template("users.html", users=all_users)


@app.route("/users/<int:id>")
def user_detail(id):
    """Retrieve a specific user's details by their ID."""
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
    conn.close()

    if user is None:
        return render_template("404.html", message=f"User with ID {id} not found."), 404

    return render_template("user_detail.html", user=user)


@app.route("/new_user", methods=["GET", "POST"])
def new_user():
    """
    GET  – Render the form to accept user input.
    POST – Validate and store the new user in the database.
    """
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        role = request.form.get("role", "").strip()

        # Basic validation
        if not name or not email or not role:
            flash("All fields are required!", "danger")
            return render_template("new_user.html", name=name, email=email, role=role)

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO users (name, email, role) VALUES (?, ?, ?)",
            (name, email, role),
        )
        conn.commit()
        conn.close()

        flash(f"User '{name}' added successfully!", "success")
        return redirect(url_for("users"))

    return render_template("new_user.html")


# Error handlers-


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 – Page / resource not found."""
    return render_template("404.html", message="The page you requested was not found."), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 – Internal server error."""
    return render_template("404.html", message="An internal server error occurred."), 500


# Run the application

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
