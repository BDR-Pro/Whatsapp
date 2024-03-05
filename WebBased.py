import pywhatkit as kit

# Specify the phone number (with country code) and the message
phone_number = "+966112170638" 
message = "100% الكود شغال ان شاء الله"

# Send the message instantly
kit.sendwhatmsg_instantly(phone_number, message)