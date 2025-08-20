import requests
import os
from dotenv import load_dotenv
import streamlit as st
import matplotlib.pyplot as plt

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY") # Retrieve the API key

def get_geocoding_data(city_name, state_code):
    """
    Return a dictionary containing the data returned by OpenWeather's Geocoding API for the given city and state code.
    
    Parameters:
    - city_name (str): The name of the US city.
    - state_code (str): The state code of the US city.
    
    Returns:
    - geocoding_response (dict): A dictionary containing the geocoding data returned by OpenWeather's Geocoding API.
    """
    geocoding_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{1}&limit={1}&appid={api_key}")
    return geocoding_response.json()

def get_weather_data(latitude, longitude):
    """
    Return a dictionary containing the data returned by the OpenWeather's Current Weather API for the given latitude and longitude.
    
    Parameters:
    - latitude (float): The latitude of the city.
    - longitude (float): The longitude of the city.
    
    Returns:
    - weather_response (dict): A dictionary containing the current weather data returned by OpenWeather's Current Weather API.
    """
    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}")
    return weather_response.json()

def report_temperature(temperature_celsius):
    """
    Report the temperature in Celsius.
    
    Parameters:
    - temperature_celsius (float): The temperature in Celsius.
    
    Returns:
    - None
    """
    st.title(f"Temperature: {temperature_celsius:.2f}°C 🌡")
    fig, ax = plt.subplots(figsize=(0.375, 1.25))
    ax.bar(0, temperature_celsius, color='red')
    ax.set_ylim(0, 50) # Assume a max temperature of 50°C for visualization
    ax.set_ylabel('Temperature (°C)')
    ax.set_xticks([])
    st.pyplot(fig)

def report_humidity(humidity):
    """
    Report the humidity percentage.

    Parameters:
    - humidity (int): The humidity percentage.

    Returns:
    - None
    """
    st.title(f"Humidity: {humidity}% 💧")
    fig, ax = plt.subplots()
    ax.pie([humidity, 100 - humidity], labels=[str(humidity) + "%",""], colors=["blue","gray"], autopct=None, textprops={'color': 'blue'})
    st.pyplot(fig)

def report_description(description, description_icon):
    """
    Report the weather description.

    Parameters:
    - description (str): A description of the weather conditions.
    - description_icon (str): The icon representing the weather conditions.

    Returns:
    - None
    """
    st.title(f"Description: {description.title()}") # Capitalize the first letter of each word of the description using title()
    st.image(f"https://openweathermap.org/img/wn/{description_icon}@4x.png", use_container_width=True)

def report_weather(temperature_celsius, humidity, description, description_icon):
    """
    Print the weather report for the given temperature, humidity, description, and description icon.
    
    Parameters:
    - temperature_celsius (float): The temperature in Celsius.
    - humidity (int): The humidity percentage.
    - description (str): A description of the weather conditions.
    - description_icon (str): The icon representing the weather conditions.
    
    Returns:
    - None
    """
    st.title(f"Weather Report for {city_name}, {state_code}: ")
    report_temperature(temperature_celsius)
    report_humidity(humidity)
    report_description(description, description_icon)

# Main program execution
st.title("Weather Report App")
st.write("Welcome to the Weather Report App! This program provides the current weather information of any city in the U.S.")
city_info = st.text_input("Please enter the U.S. city you want to check the weather for (city name, state code): ", key="city_info").strip()
city_name, _, state_code = city_info.partition(",")

if city_info: # Ensure that the user input is not empty before proceeding
    geocoding_data = get_geocoding_data(city_name, state_code)

    latitude = geocoding_data[0]['lat']
    longitude = geocoding_data[0]['lon']

    weather_data = get_weather_data(latitude, longitude)

    temperature_kelvin = weather_data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15 # Convert the temperature from Kelvin to Celsius
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    description_icon = weather_data['weather'][0]['icon']

    report_weather(temperature_celsius, humidity, description, description_icon)