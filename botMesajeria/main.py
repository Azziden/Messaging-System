import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
source_mail = os.environ['EMAIL']
password = os.environ['PASSWORD']

# Gmail SMTP Server Settings
server_smtp = 'smtp.gmail.com'
port_smtp = 587

# Create a MIME message object
message = MIMEMultipart()
message['From'] = source_mail
message['To'] = 'addressee@example.com'
message['Subject'] = 'Email Subject'

# Email Body
body = 'This is the body of the email.'
message.attach(MIMEText(body, 'plain'))

# Create a connection to the Gmail SMTP server
smtp_server = smtplib.SMTP(server_smtp, port_smtp)
smtp_server.starttls()

# Sign in to the email account
smtp_server.login(source_mail, password)

# Send the email
texto = message.as_string()
smtp_server.sendmail(source_mail, 'addressee@example.com', texto)

# Close the connection to the SMTP server
smtp_server.quit()
