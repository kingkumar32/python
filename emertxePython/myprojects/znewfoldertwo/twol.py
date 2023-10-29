import pywhatkit as kit

# Define the recipient's phone number (with country code) and the message
phone_number = "+918248962956"  # Replace with the recipient's phone number
message = "Hello, this is a test message."

# Send the message
try:
    kit.sendwhatmsg(phone_number, message)
    print(f"Message sent successfully.")
except Exception as e:
    print(f"Failed to send message. Error: {e}")
