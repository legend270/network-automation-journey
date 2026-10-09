# Network Automation Tool v2.0

A Python-based network automation learning project that demonstrates device inventory management, simulated Cisco IOS-style command execution, result collection, and automated report generation.

## Project Overview

This project explores how Python can help organize network devices and automate repetitive network management tasks.

The tool maintains a list of network devices, assigns simulated device statuses, processes predefined commands, collects results, and generates a text report.

It is part of my ongoing journey in Telecommunications Engineering, Computer Networking, Python Programming, and Network Automation.

**Current status:** Simulation mode. This version does not establish SSH connections to real routers or switches.

## Features

* **Device inventory:** Organizes network devices and their details.
* **Device status simulation:** Demonstrates online and offline device states.
* **Command processing:** Simulates selected Cisco IOS-style commands.
* **Result collection:** Organizes simulated command outputs by device.
* **Automated reporting:** Saves results to `network_report.txt`.
* **Summary statistics:** Displays the number of online and offline devices.

## Technologies Used

* Python 3
* Python `datetime` module
* Python lists and dictionaries
* Functions and loops
* Conditional statements
* File handling
* Cisco IOS concepts

## Project Structure

```text
Network_automation/
├── network_automation.py
├── network_report.txt
└── README.md
```

`network_automation.py` contains the program logic.

`network_report.txt` contains the generated report after the program runs.

## Requirements

* Python 3 installed on your computer.
* A code editor or terminal.
* No additional Python packages are required if the script uses only Python's standard library.

## How to Run

1. Open a terminal in the project directory.

2. Confirm Python is installed:

   ```bash
   python --version
   ```

3. Run the program:

   ```bash
   python network_automation.py
   ```

4. Review the displayed device statuses, simulated command results, and summary.

5. Open `network_report.txt` to inspect the generated report.

If your Windows installation uses the Python launcher, you can use `py` instead of `python`.

## Example Output

The following is an illustrative example of the type of summary the program can produce:

```text
NETWORK AUTOMATION TOOL v2.0

Device Summary
--------------
Total Devices: 3
Online Devices: 2
Offline Devices: 1

Report saved to: network_report.txt
```

**Note:** This is an illustrative summary, not a guarantee of the exact output. Device names, command results, formatting, and counts depend on the program's configured data.

## Understanding Simulation Mode

Simulation mode allows the workflow to be developed and tested without connecting to physical or virtual network devices.

In this version:

* Device statuses are simulated.
* Cisco-style command responses are simulated.
* No live router or switch configuration is changed.
* The generated report reflects the program's simulated data.

This distinction is important because simulated output should not be interpreted as evidence of live device monitoring.

## Future Improvements

Planned development goals include:

1. Improve input validation and error handling.
2. Allow users to add devices and commands more flexibly.
3. Add timestamps and clearer error reporting to generated reports.
4. Integrate with an appropriate authorized Cisco lab through SSH.
5. Collect actual device command output when a supported live connection is available.
6. Separate simulation mode from live-device mode.

Any live integration will be tested separately and clearly identified in the documentation.

## Learning Outcomes

This project provides practical experience with:

* Python functions, loops, and conditional logic.
* Lists and dictionaries for inventory management.
* File handling and automated report generation.
* Network device management concepts.
* The distinction between simulated automation and live network operations.

## Author

Telecommunications Engineering student at KNUST, developing practical skills in Python, computer networking, and network automation.

GitHub: https://github.com/legend270
