import uuid
from uuid import UUID

from pydantic import BaseModel
from sqlmodel import SQLModel
from app.models.car_brand import CarBrand
from app.models.car_model import CarModel
from app.models.car_state import CarState
from app.models.release_year import ReleaseYear

class Car(SQLModel, table=True):
    id : UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    model : CarModel
    brand: CarBrand
    release_year: ReleaseYear
    car_state : CarState
    total_car_number  : int