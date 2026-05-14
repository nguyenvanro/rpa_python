import smtplib
from email.mime.text import MIMEText

# Configuration
port = 587
smtp_server = "smtp.gmail.com"
email_login = "nguyen.van.ro.it@gmail.com"
password = "zqkg rshs xlop jrcg"

sender_email = "nguyen.van.ro.it@gmail.com"
receiver_email = "nguyenvanro.dev@gmail.com"

# Plain text content
text = """\
Hi 23CT3
"""

# Create MIMEText object
message = MIMEText(text, "plain")
message["Subject"] = "Plain text email"
message["From"] = sender_email
message["To"] = receiver_email

# Send the email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()  # Secure the connection
    server.login(email_login, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Sent')