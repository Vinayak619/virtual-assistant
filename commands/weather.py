import requests

WEATHER_API_KEY = "your_api_key"

def get_weather_report():
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/32.130153,76.414004?key={WEATHER_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["days"][0]["hours"][0]
        description = data["days"][0].get("description", "No description available")
        windspeed = weather.get("windspeed", "unknown")
        temperature = weather.get("temp", "unknown")
        humidity = weather.get("humidity", "unknown")

        report = (
            f"{description}. "
            f"The wind speed is {windspeed} miles per hour. "
            f"Temperature is {temperature} degrees Fahrenheit. "
            f"Humidity is {humidity} percent."
        )
        return report
    else:
        return "Failed to fetch weather data."
