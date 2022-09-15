from typing import Union

from pydantic import BaseModel


class MusicRecommendationsModel(BaseModel):
    city: Union[str, None] = None
    lat: Union[str, None] = None
    lon: Union[str, None] = None
