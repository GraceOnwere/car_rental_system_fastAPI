import uuid
from uuid import UUID

from app.models.car_brand import CarBrand
from app.models.car_model import CarModel
from app.models.car_state import CarState
from app.models.release_year import ReleaseYear


class Car:

    def __init__(
            self,
            model: CarModel,
            brand: CarBrand,
            release_year: ReleaseYear,
            total_car_number: int
    ):
        self.__id: UUID = uuid.uuid4()
        self.__model = model
        self.__brand = brand
        self.__release_year = release_year
        self.__car_state = CarState.AVAILABLE
        self.__total_car_number = total_car_number

    def get_id(self):
            return self.__id

    def get_car_state(self):
        return self.__car_state

    def set_car_state(self, car_state: CarState):
        self.__car_state = car_state

    def set_model(self, model):
        self.__model = model

    def set_brand(self, brand):
        self.__brand = brand

    def set_release_year(self, release_year):
        self.__release_year = release_year

    def set_total_car_number(self, total_car_number):
        self.__total_car_number = total_car_number