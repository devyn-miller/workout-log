```python
# Import necessary modules
import sqlite3
import matplotlib.pyplot as plt
from sqlite3 import Error

# Import the database module
import database

# Define the path to the SQLite database
DATABASE_PATH = "workout_planner.db"

# Function to fetch workout data for a specific exercise
def fetch_workout_data(exercise_id):
    conn = database.create_connection()
    cursor = conn.cursor()

    # Fetch the workout data for the specified exercise
    cursor.execute("""
        SELECT date, reps, weight, time, rpe
        FROM workouts
        JOIN exercises ON workouts.id = exercises.workout_id
        WHERE exercises.id = ?
        ORDER BY date
    """, (exercise_id,))

    return cursor.fetchall()

# Function to plot workout trends for a specific exercise
def plot_workout_trends(exercise_id):
    # Fetch the workout data
    data = fetch_workout_data(exercise_id)

    # Separate the data into different lists
    dates = [row[0] for row in data]
    reps = [row[1] for row in data]
    weights = [row[2] for row in data]
    times = [row[3] for row in data]
    rpes = [row[4] for row in data]

    # Create a new figure
    plt.figure()

    # Plot the number of reps over time
    plt.subplot(2, 2, 1)
    plt.plot(dates, reps)
    plt.title('Reps over time')

    # Plot the weight over time
    plt.subplot(2, 2, 2)
    plt.plot(dates, weights)
    plt.title('Weight over time')

    # Plot the time over time
    plt.subplot(2, 2, 3)
    plt.plot(dates, times)
    plt.title('Time over time')

    # Plot the RPE over time
    plt.subplot(2, 2, 4)
    plt.plot(dates, rpes)
    plt.title('RPE over time')

    # Show the plot
    plt.show()
```
