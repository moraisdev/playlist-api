from fastapi import FastAPI

from app.models.model_music import MusicRecommendationsModel
from app.services.recommendation import TrackRecommendationAPI
from app.services.get_temperature_api import OpenWeatherMapsAPI

app = FastAPI()

api_spotify = TrackRecommendationAPI()
api_weather = OpenWeatherMapsAPI()


@app.post("/music")
def read_item(item: MusicRecommendationsModel):
    tracks = []
    suggest_track = api_weather.get_type_of_track_by_temperature(
        item.city, item.lat, item.lon
    )
    tracks = api_spotify.search_recommendation(suggest_track)
    return {"tracks": tracks}
