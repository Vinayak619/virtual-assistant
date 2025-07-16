import threading
import time
from speak import speak

def set_reminder(minutes, message):
    def reminder_thread():
        time.sleep(minutes * 60)
        speak(f"Reminder: {message}")

    thread = threading.Thread(target=reminder_thread)
    thread.start()
    return f"Reminder set for {minutes} minutes to: {message}"
