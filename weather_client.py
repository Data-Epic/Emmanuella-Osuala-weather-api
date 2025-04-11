# Importing the requests module to make HTTP requests.
import requests

#  Function to get the current weather for city
def get_current_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city_name = data.get('name', city.title())
        temp = data['main']['temp']
        condition = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"\nCurrent Weather in {city_name}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Error fetching current weather for {city}. Status Code: {response.status_code}")

#  Function to get 5-day forecast
def get_forecast(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city_name = data.get('city', {}).get('name', city.title())
        print(f"\n5-Day Forecast for {city_name}:")

        for i in range(0, len(data["list"]), 8):  # 8 entries per day (3-hour intervals)
            forecast = data["list"][i]
            date = forecast["dt_txt"].split(" ")[0]
            temp = forecast["main"]["temp"]
            condition = forecast["weather"][0]["description"]

            print(f"{date}: {temp}°C, {condition}")
    else:
        print(f"Error fetching forecast for {city}. Status Code: {response.status_code}")

#  Main program
if __name__ == "__main__":
    api_key = "61a49625edd6454bfda3703b38221ac5"  # Replace with your real key if needed

    user_input = input("Enter city names (comma-separated): ")
    cities = [city.strip() for city in user_input.split(',')]

    for city in cities:
        get_current_weather(city, api_key)
        get_forecast(city, api_key)

