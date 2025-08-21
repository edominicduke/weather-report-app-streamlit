# Weather Report App

## Overview
This weather report app, developed for my AIPI 503 - Python Bootcamp class at Duke University, is intended
to report the weather information of any US city that the user prompts for by leveraging OpenWeather's Current Weather API and OpenWeather's Geocoding API. The reported information includes the current temperature, humidity, and a brief description (cloudy, clear, etc). This app is for anyone interested in checking the current weather of one or more US cities.

## Getting Started

### Prerequisites
- Python 3.10+ (Python Version Used By Project: Python 3.10.0)
- Git

### Installation/How to Set Up the Code
#### macOS/Linux
git clone https://github.com/edominicduke/weather-report-app-streamlit.git

cd weather-report-app-streamlit

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

#### Windows PowerShell
git clone https://github.com/edominicduke/weather-report-app-streamlit.git

cd weather-report-app-streamlit

python -m venv .venv

.venv\Scripts\Activate.ps1

pip install -r requirements.txt

### How to Run Web App
streamlit run report_weather.py

Then open your browser at http://localhost:8501.

### Usage
* Type the U.S. city you want to check the weather for in the format (city name, state code).
* Click the "Enter" key after doing so to see the weather report.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Additional Resources
[OpenWeather's Current Weather API](https://openweathermap.org/current)

[OpenWeather's Geocoding API](https://openweathermap.org/current#geocoding)