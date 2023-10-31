```python
# Import necessary modules
import os
import sys
import PyInstaller.__main__

# Import other parts of the application
import main

# Define the path to the main application file
MAIN_FILE_PATH = "main.py"

# Define the name of the output file
OUTPUT_FILE_NAME = "workout_planner"

# Define the path to the output directory
OUTPUT_DIRECTORY = "dist"

# Define the path to the SQLite database
DATABASE_PATH = "workout_planner.db"

# Define the path to the Kivy garden modules
KIVY_GARDEN_MODULES = os.path.join(os.path.dirname(sys.executable), 'share', 'kivy-examples', '.kivy', 'garden')

# Define the path to the Kivy data directory
KIVY_DATA_DIR = os.path.join(os.path.dirname(sys.executable), 'share', 'kivy-examples', 'data')

# Define the path to the Kivy icon
KIVY_ICON = os.path.join(os.path.dirname(sys.executable), 'share', 'kivy-examples', 'demo', 'showcase', 'data', 'icon.png')

# Define the PyInstaller options
PYINSTALLER_OPTIONS = [
    '--name=%s' % OUTPUT_FILE_NAME,
    '--onefile',
    '--windowed',
    '--add-data=%s;%s' % (DATABASE_PATH, '.'),
    '--add-data=%s;%s' % (KIVY_GARDEN_MODULES, 'garden'),
    '--add-data=%s;%s' % (KIVY_DATA_DIR, 'data'),
    '--icon=%s' % KIVY_ICON,
    MAIN_FILE_PATH,
]

# Define the main function
def main():
    # Change the current directory to the output directory
    os.chdir(OUTPUT_DIRECTORY)

    # Run PyInstaller
    PyInstaller.__main__.run(PYINSTALLER_OPTIONS)

# Call the main function
if __name__ == "__main__":
    main()
```
