"""A simple script to fetch weather information using wttr.in."""

import sys
import requests


def get_weather(city_name):
    """Fetch and print weather information for the given city."""
    try:
        url = f"https://wttr.in/{city_name}?format=3"
        response = requests.get(url, timeout=5)
        print(response.text)
    except requests.RequestException as error:
        print("Error fetching weather data:", error)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        city_arg = sys.argv[1]
        get_weather(city_arg)
    else:
        print("Usage: python app.py <city>")
