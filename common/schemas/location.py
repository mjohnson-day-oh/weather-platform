from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class Location(BaseModel):
    city: str
    state: str
    country: str
    latitude: Decimal
    longitude: Decimal
    timezone: str

class LocationResponce(Location):
    id: int
    model_config=ConfigDict(from_attributes=True)