from flask import Flask, render_template
from api import fetch_weather_data, extract_temp_humidity

app = Flask(__name__)

@app.route('/')
def home():
    # Fetch weather data for Stockholm for the first day of each month in 2023
    weather_data = fetch_weather_data()
    temps, humidities, dates = extract_temp_humidity(weather_data)
    
    return render_template('index.html', temps=temps, humidities=humidities, dates=dates)

if __name__ == '__main__':
    app.run(debug=True)