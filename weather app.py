import requests
import json

# You need to get an api key from https://openweathermap.org before you run the code.

def weather(location):
    api_key = "API_KEY_HERE" # Paste your api key as a string.
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(api_url)
    weather_data = json.loads(response.text)
    return weather_data

def display_weather(weather_data):
    
    weather_desc = weather_data["weather"][0]["description"]
    temperature = int((weather_data["main"]["temp"]) - 272)
    felt_temperature = int((weather_data["main"]["feels_like"]) - 272)
    humidity = weather_data["main"]["humidity"]
    wind_speed = (weather_data["wind"]["speed"]) * 3.6
    
    print(" ")
    print(f"Weather description: {weather_desc}")
    print(f"Temperature: {temperature}°C, temperature felt: {felt_temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} km/h")


location = input("Enter a location: ")
weather_data = weather(location)
display_weather(weather_data)