import json
from pynput import mouse

mouse_data = []

def on_click(x, y, button, pressed):
    event = f"{button} {'pressed' if pressed else 'released'} at ({x}, {y})"
    print(event)
    mouse_data.append(event)
    save_mouse_data()

def save_mouse_data():
    with open("mouse_data.json", "w") as f:
        json.dump(mouse_data, f)

def start_mouse_tracking(log_function):
    listener = mouse.Listener(on_click=on_click)
    listener.start()
