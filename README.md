# Typing Analyzer (In-App Key Events Only)

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

A lightweight **Python desktop application** that analyzes typing patterns and keyboard activity **only within the application window**.
The project demonstrates event-driven programming, GUI development with Tkinter, and data logging using JSON and CSV.

---

# Application Preview

![Typing Analyzer Interface](screenshots/app-interface.png)

The interface allows users to type text while the application tracks keyboard activity and generates useful typing statistics.

---

# Features

* Real-time typing statistics
* Keyboard event tracking within the application window
* Export typing session data
* Clean Tkinter-based GUI
* JSON and CSV export functionality

### Statistics generated

* Total key presses
* Net characters typed
* Backspace count
* Space and enter usage
* Keys per minute (KPM)
* Most frequently used characters

---

# Project Structure

```
typing-analyzer
│
├── app.py
├── analyzer.py
├── export_utils.py
├── screenshots
│   └── app-interface.png
├── README.md
├── LICENSE
└── .gitignore
```

---

# Technologies Used

* Python
* Tkinter (GUI)
* JSON (data export)
* CSV (data export)

---

# Installation

Clone the repository:

```
git clone https://github.com/joshuvavinith/keyboard-typing-analyzer.git
cd keyboard-typing-analyzer
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

# Running the Application

Run the main program:

```
python app.py
```

A desktop window will open.

### Steps to use

1. Enable the **consent checkbox**
2. Click **Start**
3. Type in the input area
4. Click **Stop** when finished
5. Export results as **JSON or CSV**

---

# Exported Files

### JSON Export

Contains typing session metadata and event logs.

Example:

```
typing_session.json
```

### CSV Export

Contains raw keyboard events.

Example:

```
typing_events.csv
```

---

# Skills Demonstrated

* Python application development
* GUI design with Tkinter
* Event-driven programming
* Data logging and serialization
* File export (JSON / CSV)
* Modular project structure

---

# Security & Ethics

This project **does not perform global keylogging**.

Keyboard events are recorded **only when typing inside the application window**, making it safe for educational and research purposes.

This project should **not be modified to monitor users without consent**.

---

# Educational Background

This project originated from a **college value-added cybersecurity course** exploring keyboard event monitoring in Python.
It has been redesigned into a **portfolio-safe typing analysis tool**.

---

# License

This project is licensed under the **MIT License**.
