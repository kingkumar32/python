import pywhatkit as kit
from datetime import datetime

now = datetime.now()
current_time_hour = now.strftime("%H")
current_time_minute = now.strftime("%M")
current_time_minute=int(current_time_minute)+1
print(current_time_minute,current_time_hour)
# Define the recipient's phone number (with country code) and the message
phone_number = "+918248962956"  # Replace with the recipient's phone number
message = "pyhton auto code test whatsappmessage"
# Schedule the message
try:
    kit.sendwhatmsg(phone_number, message,int(current_time_hour), current_time_minute)
    print(f"Message scheduled for {hour}:{minute} has been sent successfully.")
except Exception as e:
    print(f"Failed to send message. Error: {e}")
