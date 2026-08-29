from datetime import datetime

from clients import noaa

from common.schemas.weather import WeatherObservation

locations = {
    "Dayton": [39.758, -84.191]
}

def get_all_observations():
    weather_summeries: list[WeatherObservation] = []
    for location in locations.items():
        lat, lon = location[1]
        summary = noaa.get_observation(lat, lon)
        observation = WeatherObservation.model_validate(summary)
        weather_summeries.append(observation)
    return weather_summeries