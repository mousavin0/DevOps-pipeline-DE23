import sys
import os

# Add the parent directory to sys.path to make api.py discoverable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from api import extract_temp_humidity

class TestExtractTempHumidity(unittest.TestCase):
    def test_extract_temp_humidity(self):
        """Test extract_temp_humidity with example weather data."""
        # Example input data
        example_weather_data = [{
            "lat": 52.2297,
            "lon": 21.0122,
            "timezone": "Europe/Warsaw",
            "timezone_offset": 3600,
            "data": [
                {
                    "dt": 1645888976,
                    "temp": 279.13,
                    "humidity": 64,
                    "weather": [
                        {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}
                    ]
                }
            ]
        }]

        # Expected output
        expected_temps = [279.13]
        expected_humidities = [64]
        expected_dates = ["2022-02-26"]  # Convert 1645888976 to human-readable date

        # Test the function
        temps, humidities, dates = extract_temp_humidity(example_weather_data)

        # Assertions
        self.assertEqual(temps, expected_temps)
        self.assertEqual(humidities, expected_humidities)
        self.assertEqual(dates, expected_dates)

if __name__ == "__main__":
    unittest.main()
