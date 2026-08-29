from sre_parse import parse

import requests


def parse_value(metric_dict, unit_label: str =""):
    if metric_dict and metric_dict.get("value") is not None:
        return f"{round(metric_dict['value'], 2)} {unit_label}"
    return "N/A"
def get_observation(latitude: float, longitude: float):
    # latitude = 39.758
    # longitude = -84.191
    
    headers = {"User-Agent": "WeatherCollectorService"}
    
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    url2 = "https://api.weather.gov/gridpoints/ILN/44,69/stations"
    url3 = "https://api.weather.gov/stations/KCRW/observations/latest"
    response = requests.get(
        url,
        headers=headers
    )
    response_json = response.json()
    stationUrl = response_json["properties"]["observationStations"]
    # print(points)
    station_response = requests.get(
        stationUrl,
        headers=headers
    )
    station_response_json = station_response.json()
    closest_station_url = station_response_json["features"][0]["id"]
    latest_obs_url = f"{closest_station_url}/observations/latest"
    obs_response = requests.get(
        latest_obs_url,
        headers=headers
    )
    obs_json = obs_response.json()
    obs_data = obs_json["properties"]
    
    weather_summary = {
        "Observed At": obs_data.get("timestamp"),
        "Temperature": parse_value(obs_data.get("temperature"), "C"),
        "Humidity": parse_value(obs_data.get("relativeHumidity"), "%"),
        "Pressure": parse_value(obs_data.get("barometricPressure"), "Pa"),
        "Wind Speed": parse_value(obs_data.get("windSpeed"), "km/h"),
        "Rainfall" : parse_value(obs_data.get("precipitationLastHour"), "m"),
        "UV Index": "placeholder",
        "Weather Condition": "placeholder"
    }
    print(weather_summary)
    return weather_summary