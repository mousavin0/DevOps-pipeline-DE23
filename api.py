import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

LAT = 59.3293  # Latitude for Stockholm
LON = 18.0686  # Longitude for Stockholm
API_KEY = os.getenv("OPENWEATHER_API_KEY")


from datetime import datetime, timezone, timedelta
import calendar

def generate_last_12_month_timestamps():
    timestamps = []
    today = datetime.now(timezone.utc)

    for i in range(12):
        # Calculate the first day of each previous month
        first_day = today.replace(day=1) - timedelta(days=30 * i)  # Roughly going back month-by-month
        first_day = first_day.replace(day=1, hour=0, minute=0, second=0, microsecond=0)  # Set to midnight, UTC
        
        # Add timestamp for API call
        timestamps.append(int(first_day.timestamp()))
    
    # Reverse list to start from the oldest to the newest month
    timestamps.reverse()
    return timestamps


def fetch_weather_data():
    timestamps = generate_last_12_month_timestamps()
    weather_data = []

    for ts in timestamps:
        url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={LAT}&lon={LON}&dt={ts}&appid={API_KEY}&units=metric"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data.append(data)
        else:
            print(f"Failed to fetch data for timestamp {ts}, status code: {response.status_code}")

    return weather_data


def extract_temp_humidity(weather_data):
    temps, humidities, dates = [], [], []

    for data in weather_data:
        if 'data' in data:
            for entry in data['data']:
                temps.append(entry['temp'])
                humidities.append(entry['humidity'])
                
                # Convert Unix timestamp to a readable date format
                readable_date = datetime.utcfromtimestamp(entry['dt']).strftime('%Y-%m-%d')
                dates.append(readable_date)
        else:
            print("Warning: 'data' key missing in weather data response:", data)

    return temps, humidities, dates
