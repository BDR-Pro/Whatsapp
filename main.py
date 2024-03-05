from twilio.rest import Client
#load environment variables
from dotenv import load_dotenv
import os
load_dotenv()

# Your Account SID from twilio.com/console
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
# Your Auth Token from twilio.com/console
auth_token =  os.getenv('TWILIO_AUTH_TOKEN')

from_whatsapp_number=os.getenv('TWILIO_FROM_WHATSAPP_NUMBER')

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_=from_whatsapp_number,  # Twilio WhatsApp number
    body='Hello, this is a message from Python!',  # Message body
    to='whatsapp:+966XXXXXXXX'  # Your phone number with country code
)
print(f"Sid = {message.sid}")
print(f"Status = {message.status}")
print(f"Price = {message.price}")
print('Message sent successfully')