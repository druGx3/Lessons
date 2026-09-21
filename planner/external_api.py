import requests
import csv
from dotenv import load_dotenv
import os
import datetime

from requests import RequestException

# Git test
def write_error_log(log_data):
    with open("error.log", "a", encoding="utf-8") as file:
        error_text = f"{log_data.get('city')} | {log_data.get('status_code')} | {log_data.get('timestamp')} | {log_data.get('message')}\n"
        file.write(error_text)

def fetch_weather(city):

    params = {
        "key": api_key,
        "q": city
    }

    try:
        response = requests.get(url, params=params, timeout=2)
        return response, None
    except RequestException as error:
        return None, error

def record_error(message, city, status_code):
    now = datetime.datetime.now()
    error_data = {
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "status_code": status_code,
        "city": city,
        "message": message
    }
    write_error_log(error_data)

def transform_weather_data(response):
    data = response.json()

    weather_data = {
        "name": data.get("location").get("name"),
        "country": data.get("location").get("country"),
        "temp_c": data.get("current").get("temp_c"),
        "humidity": data.get("current").get("humidity"),
        "text": data.get("current").get("condition").get("text"),
        "date": data.get("location").get("localtime")
    }

    return weather_data

def write_weather(transformed_data):
    fieldnames = ["name", "country", "temp_c", "humidity", "text", "date"]

    with open("weather.csv", "a", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if os.path.getsize("weather.csv") == 0:
            writer.writeheader()

        writer.writerow(transformed_data)

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

url = "https://api.weatherapi.com/v1/current.json"

city = "Saint Petersburg"

response, error = fetch_weather(city)

if response is None:
    status_code = "N/A"
    message = str(error)
    record_error(message, city, status_code)
elif response.status_code == 200:
    transformed_data = transform_weather_data(response)
    write_weather(transformed_data)
else:
    error_js = response.json()
    message = error_js.get("error").get("message")
    status_code = response.status_code
    record_error(message, city, status_code)








