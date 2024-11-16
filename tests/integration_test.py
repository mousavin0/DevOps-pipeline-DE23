import unittest
from api import fetch_weather_data

class TestFetchWeatherData(unittest.TestCase):
    def test_fetch_weather_data(self):
        """
        Integration test for fetch_weather_data.
        Ensures the function interacts with the OpenWeather API and returns valid data.
        Requires a valid OPENWEATHER_API_KEY in the environment.
        """
        # Call the function
        weather_data = fetch_weather_data()

        # Assertions
        self.assertIsInstance(weather_data, list)  # Ensure a list is returned
        self.assertTrue(len(weather_data) > 0)  # Ensure the list is not empty

        # Validate structure of the first entry
        first_entry = weather_data[0]
        self.assertIn("data", first_entry)  # Ensure 'data' key is present
        self.assertTrue(len(first_entry["data"]) > 0)  # Ensure 'data' contains entries

if __name__ == "__main__":
    unittest.main()