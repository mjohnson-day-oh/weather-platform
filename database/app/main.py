from datetime import datetime
from decimal import Decimal

from fastapi import Depends, FastAPI
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session

# from common.schemas.location import Location
from common.schemas.weather import WeatherObservation

from .database import Base, engine, get_db
from .model import WeatherObservations

Base.metadata.create_all(bind=engine)
app = FastAPI()

class ObservationResponse(WeatherObservation):
    id: int
    
    model_config = ConfigDict(from_attributes = True)

@app.post("/weather-observations", response_model=ObservationResponse)
def create_observation(item: WeatherObservation, db: Session = Depends(get_db)):
    db_item = WeatherObservations(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# def main():
#     dayton_location = {
#         "city": "Dayton",
#         "state": "Ohio",
#         "latitude": Decimal("39.758"),
#         "longitude": Decimal("-84.191"),
#         "timezone": "GMT-4"
#     }
#     valid_location = Location.model_validate(dayton_location)