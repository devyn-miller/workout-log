```python
# Import necessary modules
import sqlite3
from sqlite3 import Error

# Import the database module
import database

# Define the path to the SQLite database
DATABASE_PATH = "workout_planner.db"

# Function to create a new workout template
def create_template(name, exercises):
    conn = database.create_connection()
    cursor = conn.cursor()

    # Insert the new template into the templates table
    cursor.execute("""
        INSERT INTO templates (name)
        VALUES (?)
    """, (name,))

    # Get the id of the newly inserted template
    template_id = cursor.lastrowid

    # Insert the exercises into the exercises table
    for exercise in exercises:
        cursor.execute("""
            INSERT INTO exercises (name, sets, reps, weight, time, rpe, template_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (exercise['name'], exercise['sets'], exercise['reps'], exercise['weight'], exercise['time'], exercise['rpe'], template_id))

    # Commit the changes and close the connection
    conn.commit()
    database.close()

# Function to edit a workout template
def edit_template(template_id, name, exercises):
    conn = database.create_connection()
    cursor = conn.cursor()

    # Update the template in the templates table
    cursor.execute("""
        UPDATE templates
        SET name = ?
        WHERE id = ?
    """, (name, template_id))

    # Delete the old exercises
    cursor.execute("""
        DELETE FROM exercises
        WHERE template_id = ?
    """, (template_id,))

    # Insert the new exercises into the exercises table
    for exercise in exercises:
        cursor.execute("""
            INSERT INTO exercises (name, sets, reps, weight, time, rpe, template_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (exercise['name'], exercise['sets'], exercise['reps'], exercise['weight'], exercise['time'], exercise['rpe'], template_id))

    # Commit the changes and close the connection
    conn.commit()
    database.close()

# Function to delete a workout template
def delete_template(template_id):
    conn = database.create_connection()
    cursor = conn.cursor()

    # Delete the template from the templates table
    cursor.execute("""
        DELETE FROM templates
        WHERE id = ?
    """, (template_id,))

    # Delete the exercises associated with the template
    cursor.execute("""
        DELETE FROM exercises
        WHERE template_id = ?
    """, (template_id,))

    # Commit the changes and close the connection
    conn.commit()
    database.close()
```
