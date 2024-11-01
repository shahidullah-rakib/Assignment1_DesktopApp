import json
import psutil
from datetime import datetime

app_data = {}

def update_app_stats(app_name, action):
    if action == "open":
        if app_name not in app_data:
            app_data[app_name] = {"count": 0, "start_time": None, "duration": 0}
        app_data[app_name]["count"] += 1
        app_data[app_name]["start_time"] = datetime.now().isoformat()
    elif action == "close":
        if app_name in app_data and app_data[app_name]["start_time"] is not None:
            duration = (datetime.now() - datetime.fromisoformat(app_data[app_name]["start_time"])).total_seconds()
            app_data[app_name]["duration"] += duration
            app_data[app_name]["start_time"] = None
        save_app_data()

def save_app_data():
    with open("app_data.json", "w") as f:
        json.dump(app_data, f)

def start_app_tracking(log_function):
    last_seen_apps = set()
    
    try:
        while True:
            current_apps = {proc.info['name'] for proc in psutil.process_iter(attrs=['name'])}
            opened_apps = current_apps - last_seen_apps
            for app in opened_apps:
                print(f"Application opened: {app}")
                update_app_stats(app, "open")

            closed_apps = last_seen_apps - current_apps
            for app in closed_apps:
                print(f"Application closed: {app}")
                update_app_stats(app, "close")

            last_seen_apps = current_apps

    except KeyboardInterrupt:
        print("Application tracking stopped.")
        save_app_data()
