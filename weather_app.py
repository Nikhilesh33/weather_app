# -*- coding: utf-8 -*-
"""weather_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gluwu2reMpnBfoyJGMOAJ67NhnzQ4CEi
"""

import requests

def get_weather_data(city):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    return response.json()

def get_weather_by_date(data, target_date):
    for entry in data["list"]:
        if entry["dt_txt"].startswith(target_date):
            return entry["main"]["temp"]
    return None

def get_wind_speed_by_date(data, target_date):
    for entry in data["list"]:
        if entry["dt_txt"].startswith(target_date):
            return entry["wind"]["speed"]
    return None

def get_pressure_by_date(data, target_date):
    for entry in data["list"]:
        if entry["dt_txt"].startswith(target_date):
            return entry["main"]["pressure"]
    return None

def main():
    city = "London,us"
    weather_data = get_weather_data(city)

    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            target_date = input("Enter the date (YYYY-MM-DD format): ")
            temperature = get_weather_by_date(weather_data, target_date)
            if temperature is not None:
                print(f"Temperature on {target_date}: {temperature}°C")
            else:
                print("No data available for the specified date.")
        elif choice == "2":
            target_date = input("Enter the date (YYYY-MM-DD format): ")
            wind_speed = get_wind_speed_by_date(weather_data, target_date)
            if wind_speed is not None:
                print(f"Wind Speed on {target_date}: {wind_speed} m/s")
            else:
                print("No data available for the specified date.")
        elif choice == "3":
            target_date = input("Enter the date (YYYY-MM-DD format): ")
            pressure = get_pressure_by_date(weather_data, target_date)
            if pressure is not None:
                print(f"Pressure on {target_date}: {pressure} hPa")
            else:
                print("No data available for the specified date.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()