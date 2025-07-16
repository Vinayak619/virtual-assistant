import pywhatkit
from speak import speak

contacts = {
   # Enter name and phone number with country code to whome you want to send message
   # eg:  "Sydney Sweeney" : "+19876543210"
}

def send_message(name, message):
    number = contacts.get(name.lower())
    if not number:
        speak(f"I don't have the contact info for {name}")
        return

    try:
        pywhatkit.sendwhatmsg_instantly(number, message, wait_time=10)
        speak(f"Message sent to {name}.")
    except Exception as e:
        print("WhatsApp error:", e)
        speak("There was an error sending the message.")
