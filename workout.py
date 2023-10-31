```python
# Import necessary modules
import sqlite3
from sqlite3 import Error

# Import the database module
import database

# Define the path to the SQLite database
DATABASE_PATH = "workout_planner.db"

# Function to add a new workout
def add_workout(date, template_id, exercises):
    conn = database.create_connection()
    cursor = conn.cursor()

    # Insert the new workout into the workouts table
    cursor.execute("""
        INSERT INTO workouts (date, template_id)
        VALUES (?, ?)
    """, (date, template_id))

    # Get the id of the newly inserted workout
    workout_id = cursor.lastrowid

    # Insert the exercises into the workout_exercises table
    for exercise in exercises:
        cursor.execute("""
            INSERT INTO workout_exercises (workout_id, exercise_id, sets, reps, weight, time, rpe)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (workout_id, exercise['id'], exercise['sets'], exercise['reps'], exercise['weight'], exercise['time'], exercise['rpe']))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Function to get all workouts
def get_workouts():
    conn = database.create_connection()
    cursor = conn.cursor()

    # Select all workouts from the workouts table
    cursor.execute("""
        SELECT * FROM workouts
    """)

    # Fetch all rows
    workouts = cursor.fetchall()

    # Close the connection
    conn.close()

    # Return the workouts
    return workouts

# Function to get a specific workout
def get_workout(workout_id):
    conn = database.create_connection()
    cursor = conn.cursor()

    # Select the workout from the workouts table
    cursor.execute("""
        SELECT * FROM workouts
        WHERE id = ?
    """, (workout_id,))

    # Fetch the row
    workout = cursor.fetchone()

    # Close the connection
    conn.close()

    # Return the workout
    return workout

# Function to delete a workout
def delete_workout(workout_id):
    conn = database.create_connection()
    cursor = conn.cursor()

    # Delete the workout from the workouts table
    cursor.execute("""
        DELETE FROM workouts
        WHERE id = ?
    """, (workout_id,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
```
