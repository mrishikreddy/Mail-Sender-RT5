# Daily Tasks Mail Sender

Welcome to the **Daily Task Email Reminder** project, a Python-based application that sends automated daily task reminders via email. Using SMTP and Gmail's secure server, this script delivers a formatted HTML email listing tasks for the current day. It's a simple yet effective tool for personal task management or sending reminders to others.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Configuration](#configuration)

## Features
- **Automated Email Sending**: Sends a daily task reminder email using Gmail's SMTP server.
- **HTML Email Content**: Delivers a styled HTML email with a task list, greetings, and motivational messages.
- **Dynamic Task Management**: Retrieves tasks based on the current date from a predefined dictionary.
- **Secure Connection**: Uses SSL for secure email transmission.
- Built with standard Python libraries: `smtplib`, `email`, `ssl`, `datetime`, and `os`.

## Installation
To set up the **Daily Task Email Reminder** project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mrishikreddy/Mail-Sender-RT5.git
   cd daily-task-email-reminder
   ```

2. **Install Dependencies**:
   The script uses Python's standard libraries (`smtplib`, `email`, `ssl`, `datetime`, `os`), so no external packages are required. Ensure you have Python 3.6+ installed.

3. **Configure Environment Variables**:
   Set up the following environment variables for email authentication and recipient details:
   - `SENDER_MAIL`: Your Gmail address (e.g., `yourname@gmail.com`).
   - `SENDER_PASSWORD`: Your Gmail App Password (see [Configuration](#configuration) for details).
   - `DESTINATION_MAIL`: The recipient's email address.
   
   On Linux/Mac:
   ```bash
   export SENDER_MAIL="yourname@gmail.com"
   export SENDER_PASSWORD="your-app-password"
   export DESTINATION_MAIL="recipient@example.com"
   ```
   On Windows (Command Prompt):
   ```cmd
   set SENDER_MAIL=yourname@gmail.com
   set SENDER_PASSWORD=your-app-password
   set DESTINATION_MAIL=recipient@example.com
   ```

4. **Run the Script**:
   Execute the Python script:
   ```bash
   python task_reminder.py
   ```

## Usage
Running the script sends an email to the specified recipient with a list of tasks for the current day. The email includes:
- A greeting ("Hello Boss!").
- A list of tasks (or "No tasks for today" if none are defined).
- A motivational message ("Happy coding 😊").

To customize tasks, edit the `d` dictionary in the script with tasks for specific dates (format: `DDMM`). Example:
```python
d = {
    "0105": ["Complete project proposal", "Attend team meeting"],
    "0205": ["Review code", "Update documentation"]
}
```

To automate daily emails, schedule the script using a task scheduler:
- **Linux/Mac**: Use `cron` (e.g., `crontab -e` and add `0 8 * * * /usr/bin/python3 /path/to/task_reminder.py` for 8 AM daily).
- **Windows**: Use Task Scheduler to run the script daily.

## How It Works
The script automates sending a daily task reminder email. Here's a breakdown:

### Task Retrieval
- **Date**: Uses `datetime` to get the current day and month (`DDMM` format).
- **Task Dictionary**: Retrieves tasks from a dictionary (`d`) using the current date as the key. Defaults to "No tasks for today" if no tasks are defined.

### Email Composition
- **Content**: Creates an HTML email with a heading, task list, and motivational message.
- **MIME Structure**: Uses `MIMEMultipart` and `MIMEText` to format the email with HTML content.
- **Headers**: Sets sender name, email, recipient, and subject using `formataddr` and `Header`.

### Email Sending
- **SMTP Connection**: Establishes a secure SSL connection to Gmail's SMTP server (`smtp.gmail.com`, port 465).
- **Authentication**: Logs in using the sender's email and app password.
- **Transmission**: Sends the email using `server.sendmail`.

## Configuration
To use Gmail for sending emails, you need an **App Password** due to Gmail's security settings:
1. Enable 2-Step Verification on your Google Account.
2. Go to [Google Account Security](https://myaccount.google.com/security).
3. Under "Signing in to Google," select "App passwords."
4. Generate a new app password for "Mail" and use it as `SENDER_PASSWORD`.
5. Store sensitive information (email, password) in environment variables, not directly in the code.
