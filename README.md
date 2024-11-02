# Activity Tracker Application

This project is an activity-tracking application designed to monitor and log various types of user activities, including mouse and keyboard interactions, application usage, and browser history. The application consists of a **backend** for tracking activities and a **frontend** to display the logged information.

## Table of Contents

- [Folder Structure](#folder-structure)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Run Instructions](#run-instructions)
- [Features](#features)
- [Project Details](#project-details)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)

---

## Folder Structure

- **backend/**: Contains all backend tracking scripts and dependencies.

  - `main.py`: The main Python script that runs backend tracking using PyQt and other libraries.
  - `requirements.txt`: Lists Python dependencies required to run the backend.

- **frontend/**: Contains the frontend for displaying tracked data with Electron.
  - `main.js`: Main Electron script to create the application window and manage processes.
  - `index.html`: Core HTML structure for the frontend UI.
  - `package.json`: Configuration file for Node.js, listing dependencies and scripts for Electron.
  - `styles.css`: CSS file to style the frontend UI.
  - `script.js`: Frontend logic and renderer process for displaying and handling tracked data.

---

## Technologies Used

- **Backend**:

  - `pynput`: Used to monitor mouse and keyboard events.
  - `PyQt5`: Provides a GUI interface for displaying tracking data.
  - `psutil`: Used for system and process utilities to track application usage.
  - `pywin32`: Enables interaction with Windows-specific APIs, useful for process and window management.

- **Frontend**:
  - `Electron.js`: Used for building cross-platform desktop applications, enabling a modern UI for displaying tracked activity logs.

---

## Setup and Installation

### Prerequisites

1. **Python**: Ensure Python 3.x is installed for running the backend.
2. **Node.js and npm**: Required for the frontend.

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   pip install -r requirements.txt
   python main.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   npm install
   npm start
   ```

## Run Instructions

### Start the Backend

1. Run the backend to start activity tracking
   cd backend
   python main.py

### Start the Frontend

1. Run the frontend to display activity logs
   cd frontend
   npm start

### Features

## Backend

1. Mouse Tracking: Logs mouse click events with details about button presses and release locations.
2. Keyboard Tracking: Tracks keystrokes and logs them into JSON.
3. Application Tracking: Monitors applications being opened or closed, along with timestamps.
4. URL Tracking: Retrieves recent URLs from the Chrome browser's history within the last hour.

## Frontend

1. Electron UI: A clean and responsive interface that reads and displays activity logs.
2. Log Visualization: Displays real-time or recorded activity logs fetched from backend JSON files.

### Project Details

1. Mouse Tracking (mouse_tracker.py): Utilizes pynput to listen for mouse events, appending each event to mouse_data.json.
2. Keyboard Tracking (keyboard_tracker.py): Uses pynput for listening to keypress events and logs them into keyboard_data.json.
3. Application Tracking (app_tracker.py): Uses psutil to track running applications, logging open/close events and usage duration in app_data.json.
4. URL Tracking (url_tracker.py): Monitors Chrome’s browsing history for visited URLs within the last hour and logs them to url_data.json.

## Troubleshooting

1. Permissions Issues: Make sure you have the necessary permissions to access system files and process data, especially for URL tracking on Chrome.
2. Missing Dependencies: Double-check that all required Python and Node.js packages are installed.

## Future Enhancements

1. Cross-Browser URL Tracking: Extend URL tracking to support more browsers beyond Chrome.
2. Enhanced Frontend Visualization: Implement graphs and charts to provide insights into user activity patterns.
3. Real-time Syncing: Sync the backend tracking data in real-time with the frontend UI.
