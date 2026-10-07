Network Device Availability Monitor v1.0
A simple Python-based network monitoring tool that checks whether specified IP addresses are reachable and reports their status as ONLINE or OFFLINE.
Project Overview
This project was developed as part of my Networking + Python learning journey.
The goal is to understand how Python can be used to automate basic network monitoring tasks.
Features
Monitor multiple IP addresses
Check device availability using ping
Display ONLINE/OFFLINE status
Count total devices
Count online devices
Count offline devices
Display results in a structured format
Technologies Used
Python
subprocess
Windows Command Prompt
Basic networking concepts
Example
=================================================================
             NETWORK DEVICE MONITOR v1.0
=================================================================
Device Name              IP Address        Status
-----------------------------------------------------------------
Google DNS               8.8.8.8           ONLINE
Cloudflare DNS           1.1.1.1           ONLINE
Google Secondary DNS     8.8.4.4           ONLINE
Cloudflare Secondary     1.0.0.1           ONLINE
Local Router             192.168.1.1       OFFLINE
-----------------------------------------------------------------
Total Devices : 5
Online        : 4
Offline       : 1
=================================================================
