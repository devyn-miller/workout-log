```python
# Import necessary modules
import sqlite3
from sqlite3 import Error

# Define the path to the SQLite database
DATABASE_PATH = "workout_planner.db"

# Create a connection to the SQLite database
def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        print(f"SQLite connection is established with {sqlite3.version}")
    except Error as e:
        print(e)
    return conn

# Initialize the database
def initialize():
    conn = create_connection()
    if conn is not None:
        create_tables(conn)
    else:
        print("Error! cannot create the database connection.")

# Create the necessary tables
def create_tables(conn):
    try:
        cursor = conn.cursor()

        # Create the workouts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS workouts (
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                template_id INTEGER,
                FOREIGN KEY (template_id) REFERENCES templates (id)
            )
        """)

        # Create the templates table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS templates (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)

        # Create the exercises table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS exercises (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                sets INTEGER,
                reps INTEGER,
                weight REAL,
                time INTEGER,
                rpe INTEGER,
                template_id INTEGER,
                FOREIGN KEY (template_id) REFERENCES templates (id)
            )
        """)

        print("Tables are created successfully.")
    except Error as e:
        print(e)

# Close the database connection
def close():
    conn = create_connection()
    if conn:
        conn.close()
        print("The SQLite connection is closed.")
```
