from datetime import datetime

from fastapi import Depends, FastAPI
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session

from database.database import Base, engine, get_db
from database.model import (
    WeatherObservations,
)

Base.metadata.create_all(bind=engine)
app = FastAPI()

class ObservationCreate(BaseModel):
    observed_at: datetime
    temperature: float
    humidity: float
    pressure: float
    wind_speed: float
    rainfall: float
    uv_index: float
    weather_condition: str

class ObservationResponse(ObservationCreate):
    id: int
    
    model_config = ConfigDict(from_attributes = True)

@app.post("/weather-observations", response_model=ObservationResponse)
def create_observation(item: ObservationCreate, db: Session = Depends(get_db)):
    db_item = WeatherObservations(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
