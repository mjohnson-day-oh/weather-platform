from decimal import Decimal

from sqlalchemy.orm import Session, sessionmaker

from common.schemas.location import Location

from .database import engine, get_db
from .model import Locations

dayton_location = {
    "city": str("Dayton"),
    "state": str("Ohio"),
    "country": str("United States"),
    "latitude": Decimal(39.785),
    "longitude": Decimal(-84.191),
    "timezone": str("GMT-4")
}

try:
    validated_data = Location.model_validate(dayton_location)
except Exception as e:
    print(f"there is an error {e}")

try:
    validated_data
except UnboundLocalError:
    print("vailidated data is unbound")


session = get_db()
new_location = Locations(validated_data.model_dump())
session.add(new_location)
session.commit()

