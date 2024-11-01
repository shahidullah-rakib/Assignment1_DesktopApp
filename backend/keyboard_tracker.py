import json
from pynput.keyboard import Listener, Key

keyboard_data = []

def on_press(key):
    event = f'Key pressed: {key}'
    print(event)
    keyboard_data.append(event)
    save_keyboard_data()

def on_release(key):
    event = f'Key released: {key}'
    print(event)
    keyboard_data.append(event)
    save_keyboard_data()
    if key == Key.esc:
        return False

def save_keyboard_data():
    with open("keyboard_data.json", "w") as f:
        json.dump(keyboard_data, f)

def start_keyboard_tracking(log_function):
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
