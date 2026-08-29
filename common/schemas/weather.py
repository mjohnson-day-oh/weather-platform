from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class WeatherObservation(BaseModel):
    observed_at: datetime
    temperature: float
    humidity: float = Field(ge=0, le=100)
    pressure: float
    wind_speed: float = Field(ge=0)
    rainfall: float = Field(ge=0)
    uv_index: float = Field(ge=0)
    weather_condition: str


class WeatherObservationResponse(WeatherObservation):
    id: int

    model_config = ConfigDict(from_attributes=True)