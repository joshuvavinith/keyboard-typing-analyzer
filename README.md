# Typing Analyzer (In-App Keyboard Event Logger)

A lightweight Python desktop application that records **keyboard events only inside the application window** and generates useful typing statistics.

This project was originally created as part of a **college value-added cybersecurity course**. The repository has been refactored into a **safe and ethical typing analysis tool** that avoids global keylogging and records input only within the application's text area.

---

## Features

* Capture keyboard events **only within the application window**
* Track typing metrics in real time
* Export typing session data
* Clean and simple desktop interface using Tkinter

### Typing statistics include

* Total key presses
* Net characters typed
* Backspace count
* Space and enter usage
* Keys per minute
* Most frequently used characters

---

## Project Structure

```
typing-analyzer
│
├── app.py              # Main GUI application
├── analyzer.py         # Typing statistics and event tracking
├── export_utils.py     # JSON and CSV export utilities
├── README.md
├── LICENSE
└── .gitignore
```

---

## Requirements

* Python 3.8+
* Tkinter (usually included with Python)

No external dependencies are required.

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

Create a virtual environment (recommended):

### Windows

```
python -m venv venv
venv\Scripts\activate
```

### Mac / Linux

```
python3 -m venv venv
source venv/bin/activate
```

---

## Running the Application

Run the main application file:

```
python app.py
```

A desktop window will open.

### Steps to use the app

1. Check the **consent checkbox**
2. Click **Start**
3. Type inside the text box
4. Click **Stop** to finish recording
5. Export results using **JSON or CSV**

---

## Exported Files

### JSON Export

Contains session metadata, event logs, and reconstructed typed text.

Example:

```
typing_session.json
```

### CSV Export

Contains a list of recorded keyboard events.

Example:

```
typing_events.csv
```

---

## Security & Ethics

This project **does not perform global keylogging**.

Keyboard events are captured **only when typing inside the application window**, making it suitable for educational and research purposes.

The project should **not be modified to monitor users without their knowledge or consent**.

---

## Educational Purpose

This repository was originally part of a **value-added cybersecurity course project** that explored keyboard event monitoring in Python. It has been redesigned to demonstrate:

* Python event handling
* Desktop GUI development with Tkinter
* Data logging and export
* Ethical software design considerations

---

## License

This project is licensed under the **MIT License**.

---

## Author

Developed as part of an academic learning exercise and later refined for portfolio demonstration.
