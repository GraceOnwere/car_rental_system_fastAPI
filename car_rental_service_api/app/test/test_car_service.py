from unittest import TestCase

from app.models.car import Car
from app.models.car_brand import CarBrand
from app.models.car_model import CarModel
from app.models.release_year import ReleaseYear
from app.services.car_service import CarService

class TestCarService(TestCase):

    def test_add_car(self):
        car_service = CarService()

        car = Car(
            CarModel.COROLLA,
            CarBrand.TOYOTA,
            ReleaseYear.YEAR_2016,
            5
        )

        result = car_service.add_car(car)

        self.assertEqual(car, result)

    def test_get_car(self):
            car_service = CarService()

            car = Car(
                CarModel.COROLLA,
                CarBrand.TOYOTA,
                ReleaseYear.YEAR_2016,
                5
            )

            car_service.add_car(car)

            result = car_service.get_car(car.get_id())

            self.assertEqual(car, result)
