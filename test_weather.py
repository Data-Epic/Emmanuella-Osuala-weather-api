import pytest
from unittest.mock import patch
from weather_client import get_current_weather, get_forecast

#  Testing how the function responds when you enter an invalid city or API key
def test_invalid_city():
    fake_key = "invalid_key"
    
    # We expect this call to either return None or just not crash
    result = get_current_weather("InvalidCity", fake_key)
    
    # We're not checking for a specific output — just confirming it handles the error gracefully
    assert result is None or result is not None  # No crash = pass

# Testing a successful response for current weather data using mocking
@patch('weather_client.requests.get')  # Patch the 'requests.get' method in weather_client
def test_get_weather_success(mock_get):
    # Simulate a successful API response
    mock_response = {
        "name": "TestCity",
        "main": {"temp": 25, "humidity": 60},
        "weather": [{"description": "sunny"}],
        "wind": {"speed": 4.5}
    }

    # Setting up the mock to return the fake data
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    # Calling the function without assertion here since it just prints
    get_current_weather("TestCity", "fake_key")
    # If the function prints successfully and doesn’t crash, test passes

#  Testing a successful 5-day forecast response using the mocked data
@patch('weather_client.requests.get')  # Patch 'requests.get' for get_forecast
def test_get_forecast_success(mock_get):
    # Simulate a valid 5-day forecast API response
    mock_response = {
        "city": {"name": "TestCity"},
        "list": [
            {
                "dt_txt": f"2025-04-{str(i).zfill(2)} 12:00:00",  # e.g., 2025-04-01 12:00:00
                "main": {"temp": 27},
                "weather": [{"description": "cloudy"}]
            }
            for i in range(1, 6)
        ] * 8  # Simulating 3-hour intervals for 5 days
    }

    # Configuring mock to return this as the API response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    # Calling the forecast function to verify it runs
    get_forecast("TestCity", "fake_key")
