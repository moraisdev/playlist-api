from typing import Dict, Union

import requests

from app.core.config import settings

class OpenWeatherMapsAPI:
    def __init__(self) -> None:
        self.open_weather_maps_weather_url = settings.open_weather_maps_weather_url
        self.open_weather_maps_weather_id: str = settings.open_weather_maps_weather_id

    def get_temperature_by_city(self, city: str) -> float:
        params: Dict = {"q": city}
        response_json: Dict = self.request_get_open_weather_api(params)
        return float(response_json.get("main", {}).get("temp", 30.0))

    def get_temperature_by_coordinates(self, lat: float, lon: float) -> float:
        params: Dict = {
            "lat": lat,
            "lon": lon,
        }
        response_json: Dict = self.request_get_open_weather_api(params)
        return float(response_json.get("main", {}).get("temp", 30.0))

    def get_type_of_track_by_temperature(
        self,
        city: Union[str, None] = None,
        lat: Union[float, None] = None,
        lon: Union[float, None] = None,
    ) -> str:
        temperature: float = 30.0

        if city:
            temperature = self.get_temperature_by_city(city)
        elif lat and lon:
            temperature = self.get_temperature_by_coordinates(lat, lon)

        if temperature > 30:
            return "party"
        elif temperature >= 15 and temperature < 30:
            return "pop"
        elif temperature >= 10 and temperature <= 14:
            return "rock"
        else:
            return "classical"

    def request_get_open_weather_api(self, params: Dict) -> Dict:

        response_json: Dict = {}

        url: str = f"{self.open_weather_maps_weather_url}?units=metric&appid={self.open_weather_maps_weather_id}"
        response = requests.get(url, params)

        if response.status_code == 200:
            response_json = response.json()

        return response_json
