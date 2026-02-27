"""
SQL Queries Reference (Task 2)
-------------------------------
These are the equivalent SQL queries used in the project.
(SQLite syntax — nearly identical to MySQL.)

-- 1. Create the "users" table
CREATE TABLE IF NOT EXISTS users (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    role  VARCHAR(50)  NOT NULL
);

-- 2. Insert sample data into the "users" table
INSERT INTO users (name, email, role) VALUES ('Alice Johnson', 'alice@example.com', 'Developer');
INSERT INTO users (name, email, role) VALUES ('Bob Smith',     'bob@example.com',   'Designer');
INSERT INTO users (name, email, role) VALUES ('Charlie Brown', 'charlie@example.com','Manager');
INSERT INTO users (name, email, role) VALUES ('Diana Prince',  'diana@example.com', 'Developer');
INSERT INTO users (name, email, role) VALUES ('Eve Davis',     'eve@example.com',   'Tester');

-- 3a. Retrieve all users from the "users" table
SELECT * FROM users;

-- 3b. Retrieve a specific user by their ID (e.g., ID = 1)
SELECT * FROM users WHERE id = 1;
"""
