import speech_recognition as sr
import pyttsx3
import webbrowser
from commands.web_opener import open_website
from commands.music_player import play_song
from commands.news import get_top_headlines
from commands.weather import get_weather_report
from commands.file_organizer import organize_file
from commands.camera import take_photo
from commands.reminder import set_reminder
from commands.whatsapp import send_message
from commands.gemini import ai_response

engine = pyttsx3.init()

latest_news = []

def speak(text):
    print(f"[SPEAK] {text}")
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    global latest_news
    command = command.lower()

    if "open" in command and "news" in command:
        for word in command.split():
            if word.isdigit():
                index = int(word) - 1
                if 0 <= index < len(latest_news):
                    speak(f"Opening news {index + 1}")
                    webbrowser.open(latest_news[index][1]) 
                    return
        speak("Sorry, I couldn't find which news you meant.")

    elif "open" in command:
        open_website(command)

    elif command.startswith("play"):
        play_song(command)

    elif "news" in command:
        latest_news = get_top_headlines() 
        if latest_news:
            for i, article in enumerate(latest_news, 1):
                speak(f"News {i}: {article[0]}")
        else:
            speak("No news available at the moment.")

    elif "weather" in command:
        report = get_weather_report()
        speak(report)
    elif any(word in command for word in ["organize", "organise", "organized", "organised", "arrange", "sort"]):
        result = organize_file()
        speak(result)
    elif "take a photo" in command or "click a picture" in command:
        result = take_photo()
        speak(result)
    elif "remind me" in command and "minute" in command:
        try:
            words = command.split()
            minutes = None
            for i, word in enumerate(words):
                if word.isdigit() and words[i+1].startswith("minute"):
                    minutes = int(word)
                    break
            if minutes:
                if "to" in command:
                    message = command.split("to", 1)[1].strip()
                    result = set_reminder(minutes, message)
                    speak(result)
                else:
                    speak("What should I remind you to do?")
            else:
                speak("Sorry, I couldn't understand the time.")
        except Exception as e:
            print("Reminder error:", e)
            speak("Sorry, there was a problem setting your reminder.")
    elif "send message in whatsapp to" in command.lower():
        try:
            words = command.split()
            name_index = words.index("to") + 1
            name = words[name_index].lower()
            if "saying" in command:
                message = command.split("saying", 1)[1].strip()
            else:
                message = "Hello from Jarvis!"
            send_message(name, message)
        except Exception as e:
            print("Error parsing WhatsApp command:", e)
            speak("Sorry, I couldn't understand the message.")
    else:
        response = ai_response(command)
        speak(response)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
            wake = recognizer.recognize_google(audio)

            if wake.lower() == "jarvis":
                speak("Yaa")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    processCommand(command)

        except Exception as e:
            print("Error:", e)
