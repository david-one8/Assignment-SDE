"""
Database Initialization Script
-------------------------------
Run this script ONCE to create the 'users' table and insert sample data.

Usage:
    python init_db.py
"""

import sqlite3

DATABASE = "users.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # SQL Query: Create the "users" table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            role  VARCHAR(50)  NOT NULL
        );
    """)

    # SQL Query: Insert sample data into the "users" table
    sample_users = [
    ("Devendra", "devendra@example.com", "Developer"),
    ("Aman", "aman@example.com", "Designer"),
    ("Tarun", "tarun@example.com", "Manager"),
    ("Toshan", "toshan@example.com", "Developer"),
    ("Om", "om@example.com", "Tester"),
]

    cursor.executemany(
        "INSERT INTO users (name, email, role) VALUES (?, ?, ?);",
        sample_users,
    )

    conn.commit()
    conn.close()
    print(f"Database '{DATABASE}' initialized with {len(sample_users)} sample users.")


if __name__ == "__main__":
    init_db()
