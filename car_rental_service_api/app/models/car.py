import uuid
from uuid import UUID

from app.models.car_brand import CarBrand
from app.models.car_model import CarModel
from app.models.car_state import CarState
from app.models.release_year import ReleaseYear


class Car:
    __id : UUID = uuid.uuid4()
    __model : CarModel = None
    __brand: CarBrand = None
    __release_year: ReleaseYear = None
    __car_state : CarState = None
    __total_car_number : int = None