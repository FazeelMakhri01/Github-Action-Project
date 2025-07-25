import sys
import requests

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        print(response.text)
    except Exception as e:
        print("Error fetching weather data:", e)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        city = sys.argv[1]
        get_weather(city)
    else:
        print("Usage: python app.py <city>")       #prints the name of the city with temperature.