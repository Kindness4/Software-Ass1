# # import sys

# # outfit_suggestions = {
# #     'sunny': 'Wear a T-shirt, shorts, and sunglasses.',
# #     'rainy': 'Bring an umbrella, wear a raincoat, and boots.',
# #     'cloudy': 'Wear a light jacket and comfortable pants.',
# #     'snowy': 'Dress warmly with a heavy coat, gloves, and boots.'
# # }

# # def suggest_outfit(weather):
# #     if weather.lower() in outfit_suggestions:
# #         return outfit_suggestions[weather.lower()]
# #     else:
# #         return "Sorry, I don't have a suggestion for that weather."

# # if __name__ == "__main__":
# #     if len(sys.argv) != 2:
# #         print("Usage: python outfit_suggestor.py <weather>")
# #     else:
# #         weather = sys.argv[1]
# #         suggestion = suggest_outfit(weather)
# #         print(f"For {weather} weather: {suggestion}")
# #import requests
# #import argparse


# # OpenWeatherMap API key
# #API_KEY = "80c78f0c7157b777b6d27ec02260eb93"  # Replace with your OpenWeatherMap API key

# # Function to fetch weather data
# #def get_weather_data(city):
#     base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
#     response = requests.get(base_url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

# # Function to suggest clothing based on weather
# #def suggest_clothing(temperature):
#     if temperature >= 25:
#         return "It's hot! Wear shorts and a t-shirt."
#     elif 15 <= temperature < 25:
#         return "Mild weather! Jeans and a light jacket should be good."
#     elif 5 <= temperature < 15:
#         return "Cool weather! Consider wearing a sweater or a hoodie."
#     else:
#         return "It's cold! Bundle up with a coat, scarf, and gloves."

# # Command-line argument parser
# def main():
#     parser = argparse.ArgumentParser(description="Get clothing suggestions based on weather.")
#     parser.add_argument("city", help="City name to get weather information for")
#     args = parser.parse_args()

#     city = args.city
#     weather_data = get_weather_data(city)

#     if weather_data:
#         temperature = weather_data["main"]["temp"] - 273.15  # Convert temperature from Kelvin to Celsius
#         description = weather_data["weather"][0]["description"]
#         print(f"Weather in {city.capitalize()}: {description.capitalize()}")
#         print(f"Temperature: {temperature:.1f}°C")
#         print(suggest_clothing(temperature))
#     else:
#         print("Failed to fetch weather data. Please check the city name or API key.")

# if __name__ == "__main__":
#     main() #"""
import requests

def get_weather_data(city):
    API_KEY = "80c78f0c7157b777b6d27ec02260eb93"  # Replace with your OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def suggest_clothing(temperature):
    if temperature >= 25:
        return "It's hot! Wear shorts and a t-shirt."
    elif 15 <= temperature < 25:
        return "Mild weather! Jeans and a light jacket should be good."
    elif 5 <= temperature < 15:
        return "Cool weather! Consider wearing a sweater or a hoodie."
    else:
        return "It's cold! Bundle up with a coat, scarf, and gloves."

def main():
    city = "London"
    weather_data = get_weather_data(city)

    if weather_data:
        temperature = weather_data["main"]["temp"] - 273.15  # Convert temperature from Kelvin to Celsius
        description = weather_data["weather"][0]["description"]
        print(f"Weather in {city.capitalize()}: {description.capitalize()}")
        print(f"Temperature: {temperature:.1f}°C")
        print(suggest_clothing(temperature))
    else:
        print("Failed to fetch weather data. Please check the city name or API key.")

if __name__ == "__main__":
    main()
