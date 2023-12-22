from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

from screeninfo import get_monitors
import threading
import time
import pynput

mouse = MouseController()
keyboard = KeyboardController()

# Global variable to control the script's running status
running = True


def click_and_press():
    # Find the center of the screen
    monitors = get_monitors()
    monitor = get_monitors()[0]
    screenWidth, screenHeight = monitor.width, monitor.height
    center_x, center_y = screenWidth / 2, screenHeight / 2
    mouse.position = (center_x, center_y)
    while running:

        if monitors:
            # Press the W key
            keyboard.press('w')
            # Left-click
            mouse.press(Button.left)


# Wait for 3 seconds
time.sleep(3)

# Start the thread
thread = threading.Thread(target=click_and_press)
thread.start()


# Keyboard listening function
def on_press(key):
    if key == Key.esc:
        # Stop the script
        global running
        running = False


# Start the keyboard listener
with pynput.keyboard.Listener(on_press=on_press) as listener:
    # Wait while the script is running
    while running:
        pass

# Wait for the thread to finish
thread.join()

# Stop the keyboard listener
listener.stop()
