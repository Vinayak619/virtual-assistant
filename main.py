import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
import time
from openai import OpenAI
import json

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "59c0577642ff439996bd363d0838c1fe"
wether_api = "GDFLHMF63QGRVTYX8Y7MHP7Y8"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def aiProcess(command):
    client = OpenAI(
    api_key="API_KEY",
                )
    completion = client.chat.completions.create(
    model="gpt-4.1-nano-2025-04-14",
    messages=[
        {"role": "system", "content" : "You are virtual assistance, skilled in general tasks."},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open chat gpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "osama" in c.lower():
        webbrowser.open("https://youtu.be/St7ny38gLp4?si=Ad83EnsdDWeW-YdV&t=10s")
    elif c.lower().startswith("play"):
        song = " ".join(c.lower().split(" ")[1:]) # ["play" ,"at", "peace"]
        try:
            link = music_library.music[song]
            webbrowser.open(link)
        except KeyError:
            speak(f"Sorry, the song '{song}' was not found in your library.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            if articles:
                speak("Here are the top headlines.")
                for article in articles[:5]:
                    print(article['title'])  
                    speak(article['title'])
                    time.sleep(1)  
    elif "weather" in c.lower():
        response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/32.130153,76.414004?key={wether_api}")
        
        if response.status_code == 200:
            data = response.json()
            try:
                weather = data["days"][0]["hours"][0]

                windspeed = weather.get("windspeed", "unknown")
                pressure = weather.get("pressure", "unknown")
                preciptype = ", ".join(weather.get("preciptype", ["none"]))
                humidity = weather.get("humidity", "unknown")
                temperature = weather.get("temp", "unknown")
                description = data["days"][0].get("description", "No description available")
                speak("Today's weather forecast is:")
                speak(f"Weather summary: {description}")
                speak(f"The wind speed is {windspeed} miles per hour, the pressure is {pressure} hectopascals, there will be {preciptype}, humidity is {humidity} percent, the temperature is {temperature} degrees Fahrenheit.")
            except Exception as e:
                print("Error extracting weather data:", e)
                speak("There was an issue reading the weather data.")
        else:
            speak("Failed to fetch weather data.")
     
    else:
        # output = aiProcess(c)
        # speak(output)
        pass
if __name__ == "__main__":  
    speak("Initializing Jarvis....")
    while True:
            # Listen to the wake word "Jarvis"
            # obtain audio from the microphone 
        r = sr.Recognizer()
         

        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=2, phrase_time_limit=1) 
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
                    print(command)
                      
        except Exception as e:
            print("Error: {0}".format(e))

 