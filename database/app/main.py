from datetime import datetime
from decimal import Decimal

from fastapi import Depends, FastAPI
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from sqlalchemy import select

# from common.schemas.location import Location
from common.schemas.weather import WeatherObservation

from .database import Base, engine, get_db, SessionLocal
from .model import WeatherObservations, Locations

SEED_LOCATIONS = (
    ("Dayton", 39.7589, -84.1916, "America/New_York"),
    ("Columbus", 39.9612, -82.9988, "America/New_York"),
    ("Chicago", 41.8781, -87.6298, "America/Chicago"),
    ("Denver", 39.7392, -104.9903, "America/Denver"),
    ("Phoenix", 33.4484, -112.0740, "America/Phoenix"),
)


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

def main() -> None:
    inserted = 0

    with SessionLocal.begin() as session:
        for city, latitude, longitude, timezone in SEED_LOCATIONS:
            existing_id = session.scalar(
                select(Locations.id).where(
                    Locations.city == city,
                    Locations.timezone == timezone,
                ).limit(1)
            )
# def main():
#     dayton_location = {
#         "city": "Dayton",
#         "state": "Ohio",
#         "latitude": Decimal("39.758"),
#         "longitude": Decimal("-84.191"),
#         "timezone": "GMT-4"
#     }
#     valid_location = Location.model_validate(dayton_location)