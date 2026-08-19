import os
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Numeric,
    String,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from database.database import Base

DB_USER = os.getenv("POSTGRES_USER", "myuser")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "mypassword")
DB_NAME = os.getenv("POSTGRES_DB", "weatherplatform")
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@db:5432/{DB_NAME}" #postgresql://myuser:mypassword@db:5432/weatherplatform

class Locations(Base):
    __tablename__: str = 'locations'
    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(String(50), unique=True)
    state: Mapped[str] = mapped_column(String(50))
    country: Mapped[str] = mapped_column(String(50))
    latitude: Mapped[Decimal] = mapped_column(Numeric(precision=4, scale=2))
    longetude: Mapped[Decimal] = mapped_column(Numeric(precision=4, scale=2))
    timezone: Mapped[str] = mapped_column(String(50))

class WeatherObservations(Base):
    __tablename__: str = 'weatherobervations'
    id: Mapped[int] = mapped_column(primary_key=True)
    observed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    teperature: Mapped[float] = mapped_column(Float)
    humidity: Mapped[float] = mapped_column(Float)
    pressure: Mapped[float] = mapped_column(Float)
    wind_speed: Mapped[float] = mapped_column(Float)
    rainfall: Mapped[float] = mapped_column(Float)
    uv_index: Mapped[float] = mapped_column(Float)
    weather_condition: Mapped[str] = mapped_column(String(100))
    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id", ondelete="CASCADE"))
    location: Mapped[Locations] = relationship(back_populates="weatherobervations")

class Users(Base):
    __tablename__: str = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50))
    password_hash: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(String(50))

class Alerts(Base):
    __tablename__: str = 'alerts'
    id: Mapped[int] = mapped_column(primary_key=True)
    metric: Mapped[str] = mapped_column(String(50))
    operator: Mapped[str] = mapped_column(String(50))
    threshold: Mapped[str] = mapped_column(Float)
    enabled: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped[Users] = relationship(back_populates="alerts")
    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id", ondelete="CASCADE"))
    location: Mapped[Locations] = relationship(back_populates="alerts")
