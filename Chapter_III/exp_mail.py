import smtplib
from email.mime.text import MIMEText

# Configuration
port = 587
smtp_server = "smtp.gmail.com"
login = "nguyenvanan@gmail.com"
password = "your_app_password"

sender_email = "nguyenvanan@gmail.com"
receiver_email = "nguyenvanba@gmail.com"

# Plain text content
text = """\
Hi,
Check out the new post on the Mailtrap blog:
SMTP Server for Testing: Cloud-based or Local?
https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
Feel free to let us know what content would be useful for you!
"""

# Create MIMEText object
message = MIMEText(text, "plain")
message["Subject"] = "Plain text email"
message["From"] = sender_email
message["To"] = receiver_email

# Send the email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()  # Secure the connection
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Sent')