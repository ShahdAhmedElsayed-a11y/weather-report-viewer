import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"


class WeatherReport:
    """بيخزن بيانات الطقس اللي رجعت من الـ API"""

    def __init__(self, city, country, temperature, feels_like, humidity, pressure, wind_speed, description):
        self.city = city
        self.country = country
        self.temperature = temperature
        self.feels_like = feels_like
        self.humidity = humidity
        self.pressure = pressure
        self.wind_speed = wind_speed
        self.description = description

    @classmethod
    def from_json(cls, data):
        return cls(
            city=data["location"]["name"],
            country=data["location"]["country"],
            temperature=data["current"]["temp_c"],
            feels_like=data["current"]["feelslike_c"],
            humidity=data["current"]["humidity"],
            pressure=data["current"]["pressure_mb"],
            wind_speed=data["current"]["wind_kph"],
            description=data["current"]["condition"]["text"],
        )

    def display(self):
        print()
        print("=" * 42)
        print(f" Weather Report: {self.city}, {self.country}")
        print("=" * 42)
        print(f" Condition   : {self.description.title()}")
        print(f" Temperature : {self.temperature} °C")
        print(f" Feels like  : {self.feels_like} °C")
        print(f" Humidity    : {self.humidity} %")
        print(f" Pressure    : {self.pressure} hPa")
        print(f" Wind speed  : {self.wind_speed} km/h")
        print("=" * 42)
        print()


def fetch_weather(city):
    params = {"key": API_KEY, "q": city}
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    if not API_KEY:
        print("Error: API_KEY not found. Check your .env file.")
        return

    print("Weather Report Viewer (type 'q' to quit)")

    while True:
        city = input("Enter city name: ").strip()

        if city.lower() == "q":
            print("Goodbye!")
            break
        if not city:
            continue

        try:
            data = fetch_weather(city)
            WeatherReport.from_json(data).display()
        except requests.exceptions.HTTPError as e:
            status = e.response.status_code
            if status == 401:
                print("Error 401: invalid API key (or not activated yet).")
            elif status == 404:
                print(f"Error 404: city '{city}' not found.")
            else:
                print(f"API error: HTTP {status}")
        except requests.exceptions.RequestException:
            print("Connection error: check your internet and try again.")


if __name__ == "__main__":
    main()
