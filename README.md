# Keyboard Typing Analyzer

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project-Completed-success)
![CI](https://github.com/joshuvavinith/keyboard-typing-analyzer/actions/workflows/python-tests.yml/badge.svg)

A lightweight **Python desktop application** that analyzes typing activity and keyboard usage patterns within the application window.

The application records keyboard events while typing, generates useful statistics, and allows exporting typing session data in **JSON and CSV formats**.

This project demonstrates **GUI development, event-driven programming, data logging, automated testing, and CI/CD integration** using GitHub Actions.

---

# Application Preview

![Typing Analyzer Interface](screenshots/app-interface.png)

The application interface allows users to start and stop typing sessions while tracking keyboard activity and generating statistics.

---

# Features

* Desktop GUI built using **Tkinter**
* Real-time typing statistics
* Keyboard event tracking within the application window
* Export typing session data
* JSON and CSV export support
* Modular Python project structure
* Automated testing using **pytest**
* Continuous Integration with **GitHub Actions**

---

# Typing Statistics Generated

The application calculates the following metrics:

* Total key presses
* Net characters typed
* Backspace usage
* Space and Enter key counts
* Keys per minute (KPM)
* Most frequently used characters

These statistics help analyze typing behavior and keyboard usage patterns.

---

# Project Structure

```text
keyboard-typing-analyzer
│
├── app.py
├── analyzer.py
├── export_utils.py
│
├── tests
│   └── test_analyzer.py
│
├── screenshots
│   └── app-interface.png
│
├── .github
│   ├── workflows
│   │   └── python-tests.yml
│   └── ISSUE_TEMPLATE
│       └── bug_report.md
│
├── CONTRIBUTING.md
├── README.md
├── LICENSE
└── .gitignore
```

---

# File Overview

### app.py

Main GUI application that handles keyboard input events and user interaction.

### analyzer.py

Processes keyboard events and computes typing statistics.

### export_utils.py

Exports session data into JSON and CSV formats.

### tests/

Contains automated tests for verifying analyzer functionality.

### .github/workflows/

Contains the GitHub Actions configuration for running automated tests.

---

# Technologies Used

* **Python**
* **Tkinter** – GUI framework
* **Pytest** – Automated testing
* **JSON / CSV** – Data export
* **GitHub Actions** – Continuous Integration

---

# Installation

Clone the repository:

```bash
git clone https://github.com/joshuvavinith/keyboard-typing-analyzer.git
cd keyboard-typing-analyzer
```

Create a virtual environment (recommended):

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install testing dependency:

```bash
pip install pytest
```

---

# Running the Application

Start the program using:

```bash
python app.py
```

A desktop window will open where you can begin a typing session.

---

# Usage

1. Enable the **consent checkbox**
2. Click **Start** to begin recording
3. Type inside the text area
4. Click **Stop** to finish the session
5. Export results as **JSON or CSV**

---

# Running Tests

Run automated tests using:

```bash
pytest
```

All tests should pass successfully.

---

# Continuous Integration

This project uses **GitHub Actions** to automatically run tests whenever code is pushed to the repository.

The CI workflow ensures:

* Code changes do not break existing functionality
* Automated tests run on each push or pull request
* The project remains stable and maintainable

---

# Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Please read **CONTRIBUTING.md** for detailed guidelines.

---

# Security and Ethics

This project **does not perform global keylogging**.

Keyboard events are captured **only within the application window**, making it safe for educational and demonstration purposes.

The software should **not be modified or used to monitor users without their consent**.

---

# Educational Context

This project originated from a **college value-added cybersecurity course assignment** focused on keyboard event monitoring in Python.

It has been redesigned into a **portfolio-friendly typing analysis tool** demonstrating good software engineering practices.

---

# License

This project is licensed under the **MIT License**.
