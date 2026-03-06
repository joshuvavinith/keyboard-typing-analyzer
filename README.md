# Keyboard Typing Analyzer

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

A lightweight **Python desktop application** that analyzes keyboard activity and typing patterns within the application window.

The application records keyboard events while the user types inside the interface, generates useful statistics, and allows exporting typing session data in **JSON and CSV formats**.

This project demonstrates GUI development, event-driven programming, and structured data logging in Python.

---

# Application Preview

![Typing Analyzer Interface](screenshots/app-interface.png)

The interface allows users to start a typing session, track keyboard activity, and export statistics.

---

# Features

* Desktop GUI built using **Tkinter**
* Real-time typing statistics
* Keyboard event tracking inside the application window
* Export typing session data
* JSON and CSV export support
* Modular Python code architecture

---

# Typing Statistics Generated

The application calculates:

* Total key presses
* Net characters typed
* Backspace usage
* Space and Enter key counts
* Keys per minute (KPM)
* Most frequently used characters

These metrics help analyze typing behavior and keyboard usage patterns.

---

# Project Structure

```id="djqynk"
keyboard-typing-analyzer
│
├── app.py
├── analyzer.py
├── export_utils.py
├── screenshots
│   └── app-interface.png
├── CONTRIBUTING.md
├── README.md
├── LICENSE
├── .github
│   └── ISSUE_TEMPLATE
│       └── bug_report.md
└── .gitignore
```

---

# File Overview

### app.py

Contains the main GUI application and handles keyboard events.

### analyzer.py

Processes keyboard events and calculates typing statistics.

### export_utils.py

Handles exporting session data to JSON and CSV formats.

---

# Technologies Used

* **Python**
* **Tkinter** for GUI development
* **JSON** for structured data storage
* **CSV** for exporting keyboard event logs

---

# Installation

Clone the repository:

```id="q9dkkv"
git clone https://github.com/joshuvavinith/keyboard-typing-analyzer.git
cd keyboard-typing-analyzer
```

Create a virtual environment (recommended):

### Windows

```id="gyb5yo"
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```id="ax3xt2"
python3 -m venv venv
source venv/bin/activate
```

---

# Running the Application

Start the program with:

```id="rmn3vd"
python app.py
```

A desktop window will open where you can start a typing session.

---

# Usage

1. Enable the **consent checkbox**
2. Click **Start** to begin recording
3. Type inside the text area
4. Click **Stop** to finish the session
5. Export results as **JSON or CSV**

---

# Exported Files

### JSON Export

Contains typing session metadata and keyboard event logs.

Example:

```id="qq5u5c"
typing_session.json
```

### CSV Export

Contains raw keyboard event records.

Example:

```id="6sv8m3"
typing_events.csv
```

---

# Contributing

Contributions are welcome.

If you'd like to improve the project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

See **CONTRIBUTING.md** for detailed guidelines.

---

# Security and Ethics

This project **does not perform global keylogging**.

Keyboard events are recorded **only within the application window**, making it safe for educational and demonstration purposes.

The software should **not be modified or used to monitor users without their consent**.

---

# Educational Context

This project originated from a **college value-added cybersecurity course assignment** focused on keyboard event monitoring in Python.

It has been redesigned into a **portfolio-friendly typing analysis tool**.

---

# License

This project is licensed under the **MIT License**.
