import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import ssl
import datetime
from email.utils import formataddr
import os 

sender_name = "Rishik Tech Assistant"
sender_email = os.getenv("SENDER_MAIL") 
sender_password = os.getenv("SENDER_PASSWORD")  
recipient_email = os.getenv("DESTINATION_MAIL")  


time = datetime.datetime.now()
ddmm = str(time.day)+str(time.month)

d = {
  
    
   
}

tasks = d.get(ddmm, ["No tasks for today"])

subject = "Your Tasks for Today"
html_content = f"""
<html>
    <body>
        <h1>Hello Boss!</h1>
        <h3>Here are your tasks for today:</h3>
        <ul>
            {''.join(f'<li>{task}</li>' for task in tasks)}
        </ul>
        <h5>Complete these tasks with first priority, Have a good day</h5> 
        <h5>Happy coding 😊</h5>
    </body>
</html>
"""


# Create the email content
message = MIMEMultipart("alternative")
message["From"] = formataddr((sender_name, sender_email))
message["To"] = recipient_email
message["Subject"] = Header(subject, "utf-8")

# Attach the HTML content to the email
html_part = MIMEText(html_content, "html", "utf-8")
message.attach(html_part)

# Establish a secure connection using SSL and send the email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())