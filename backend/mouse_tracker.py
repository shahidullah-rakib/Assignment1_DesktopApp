from pynput import mouse

class MouseTracker:
    def __init__(self, ui_update_callback):
        self.ui_update_callback = ui_update_callback

    def on_click(self, x, y, button, pressed):
        action = "pressed" if pressed else "released"
        event_text = f"{button} {action} at ({x}, {y})"
        self.ui_update_callback(event_text)

    def start_listener(self):
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()
