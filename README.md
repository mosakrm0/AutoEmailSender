# Inactive Account Email Automator 

A Python automation script designed to help IT Support teams quickly identify users who have been inactive and automatically send them a follow-up email. 

Built to streamline administrative tasks and reduce manual Excel filtering.

## Features
* **Automated Data Filtering:** Reads user data directly from an Excel file and filters out accounts that haven't logged in for 21+ days.
* **Bulk Email Sending:** Automatically dispatches customized warning emails to the filtered users.
* **Network-Safe:** Uses SSL (Port 465) to bypass common corporate firewall and ISP SMTP blocks.

## Prerequisites
Before running the script, ensure you have Python installed along with the required libraries.

Install the dependencies using your terminal or command prompt:
```bash
pip install pandas openpyxl
