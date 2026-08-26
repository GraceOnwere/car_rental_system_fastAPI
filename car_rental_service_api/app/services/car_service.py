
from app.models.car import Car
from app.models.car_state import CarState


class CarService:
    def __init__(self):
        self.cars = []


    def add_car(self, car):
        self.cars.append(car)
        return car

    def get_car (self, car_id):
        for car in self.cars:
            if car.get_id() == car_id:
                return car

    def get_all_cars(self):
        return self.cars


    def update_car(self, car):
        def update_car(
                self,
                car_id,
                model=None,
                brand=None,
                release_year=None,
                total_car_number=None
        ):
            car = self.get_car(car_id)

            if car is None:
                return None

            if model is not None:
                car.set_model(model)

            if brand is not None:
                car.set_brand(brand)

            if release_year is not None:
                car.set_release_year(release_year)

            if total_car_number is not None:
                car.set_total_car_number(total_car_number)

            return car

    def get_available_cars(self):
        return [
            car for car in self.cars
            if car.get_car_state() == CarState.AVAILABLE
        ]

    def change_car_state(self, car_state):
        return [
            car for car in self.cars
            if car.get_car_state() == CarState.AVAILABLE
        ]


    def remoe_car_by_id(self, car_id):
        car = self.get_car(car_id)

        if car is None:
            return None

        self.cars.remove(car)
        return car

    def remove_all_cars(self):
        self.cars.clear()

