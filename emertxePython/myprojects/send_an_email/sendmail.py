# import smtplib
# from email.mime.text import MIMEText

# subject = "Email Subject"
# body = "This is the body of the text message"
# sender = "ssycooking@gmail.com"
# recipients = ["sugumar2912@gmail.com", "sugumarthamizhan@gmail.com"]
# password = "SelviTamil"


# def send_email(subject, body, sender, recipients, password):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = ', '.join(recipients)
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
#        smtp_server.login(sender, password)
#        smtp_server.sendmail(sender, recipients, msg.as_string())
#     print("Message sent!")


# send_email(subject, body, sender, recipients, password)

import smtplib
from email.mime.text import MIMEText

# Set up the SMTP server
smtp_server = 'smtp.gmail.com'  # e.g., 'smtp.gmail.com' for Gmail
smtp_port = 587  # This may vary depending on your SMTP server

# Sender's credentials
sender_email = 'ssycooking@gmail.com'
sender_password = 'TamilSel'

# Recipient's email address
recipient_email = 'sugumar2912@gmail.com'

# Create a MIMEText object
message = MIMEText('Hello, this is a test email sent from Python.')

# Add the sender and recipient information to the message
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Test Email'

# Connect to the SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Use TLS encryption
    server.login(sender_email, sender_password)  # Log in to your email account
    server.sendmail(sender_email, recipient_email, message.as_string())  # Send the email

print('Email sent successfully!')


