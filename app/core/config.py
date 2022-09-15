from pydantic import BaseSettings


class SettingsEnv(BaseSettings):
    spotify_client_id: str
    spotify_client_secret: str
    spotify_url: str
    spotify_url_token: str
    open_weather_maps_weather_url: str
    open_weather_maps_weather_id: str

    class Config:
        env_file = "../.env"


settings = SettingsEnv()
