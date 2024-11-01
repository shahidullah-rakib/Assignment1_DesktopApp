import os
import sqlite3
import time
from shutil import copy2
from datetime import datetime, timedelta
import json
import threading

# Path to Chrome's history file
chrome_history_path = os.path.expanduser("~") + r"/AppData/Local/Google/Chrome/User Data/Default/History"

# JSON file to save visited URLs
json_file_path = "url_data.json"

# Initialize a set to store visited URLs to avoid duplicates
visited_urls = set()

# Initialize a list to hold log entries for JSON output
log_entries = []

def log_url(url, browser):
    """
    Logs the URL with a timestamp to a JSON structure.
    """
    entry = {
        "timestamp": datetime.now().isoformat(),
        "browser": browser,
        "url": url
    }
    log_entries.append(entry)
    print(f"{entry['timestamp']} - [{browser}] {url}")
    save_to_json()

def save_to_json():
    """
    Saves the current log entries to the JSON file.
    """
    with open(json_file_path, "w") as json_file:
        json.dump(log_entries, json_file, indent=4)
    print("Log entries saved to", json_file_path)

def fetch_chrome_history():
    """
    Fetches URLs visited in the last hour from Chrome's history database.
    """
    temp_history = "chrome_history_temp"
    one_hour_ago = (datetime.now() - timedelta(hours=1)).timestamp() * 1000000  # convert to microseconds
    try:
        copy2(chrome_history_path, temp_history)  # Make a copy of the history file
        conn = sqlite3.connect(temp_history)
        cursor = conn.cursor()
        # SQL query to get URLs visited in the last hour
        cursor.execute("SELECT url FROM urls WHERE last_visit_time >= ? ORDER BY last_visit_time DESC", (one_hour_ago,))
        urls = cursor.fetchall()
        for (url,) in urls:
            if url not in visited_urls:
                visited_urls.add(url)
                log_url(url, "Chrome")
        conn.close()
    except Exception as e:
        print(f"Error reading Chrome history: {e}")
    finally:
        if os.path.exists(temp_history):
            os.remove(temp_history)

def monitor_websites(interval=60):
    """
    Continuously monitors Chrome history for new URLs.
    """
    try:
        while True:
            fetch_chrome_history()  # Fetch recent URLs from the last hour
            time.sleep(interval)  # Check every `interval` seconds
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")

def start_url_monitoring(log_function):
    """
    Starts the URL monitoring in a separate thread.
    """
    monitoring_thread = threading.Thread(target=monitor_websites)
    monitoring_thread.daemon = True  # Daemonize thread
    monitoring_thread.start()
