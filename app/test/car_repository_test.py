import uuid

import pytest
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from app.models.car import Car
from app.models.car_brand import CarBrand
from app.models.car_model import CarModel
from app.models.car_state import CarState
from app.models.release_year import ReleaseYear
from app.repositories.car_repository import CarRepository

class TestCarRepository:

    def test_empty_repository(self,session: Session):
        repository = CarRepository(session=session)

        assert repository is not None

    def test_save_car_count_is_one(self,session: Session):
        repository = CarRepository(session=session)

        car = Car()
        car.brand = CarBrand.TOYOTA
        car.model = CarModel.CAMRY
        car.release_year = ReleaseYear.YEAR_2015
        car.plate_number = "0101"
        car.car_state = CarState.AVAILABLE

        repository.save(car)

        assert repository.count() == 1

    def test_save_two_cars_count_is_two(self,session: Session):
        repository = CarRepository(session=session)

        car = Car()
        car.brand = CarBrand.LEXUS
        car.model = CarModel.RX350
        car.release_year = ReleaseYear.YEAR_2015
        car.plate_number = "0101"

        repository.save(car)

        car_two = Car()
        car_two.brand = CarBrand.TOYOTA
        car_two.model = CarModel.CAMRY
        car_two.release_year = ReleaseYear.YEAR_2015
        car_two.plate_number = "0102"

        repository.save(car_two)
        assert repository.count() == 2

    def test_save_car_with_duplicate_plate_number_raises_error(self,session: Session):
        repository = CarRepository(session=session)

        car = Car()
        car.brand = CarBrand.TOYOTA
        car.model = CarModel.CAMRY
        car.release_year = ReleaseYear.YEAR_2015
        car.plate_number = "0101"

        repository.save(car)

        assert repository.count() == 1

        car_two = Car()
        car_two.brand = CarBrand.TOYOTA
        car_two.model = CarModel.CAMRY
        car_two.release_year = ReleaseYear.YEAR_2015
        car_two.plate_number = "0101"

        with pytest.raises(IntegrityError):
            repository.save(car_two)

    def test_save_car_with_missing_required_fields_raises_integrity_error(self,session: Session):
        repository = CarRepository(session=session)

        car = Car()
        car.brand = CarBrand.LEXUS
        car.model = CarModel.RX350

        with pytest.raises(IntegrityError):
            repository.save(car)

    def test_find_by_id_returns_valid_car(self,session: Session):
        repository = CarRepository(session=session)

        car = Car()
        car.brand = CarBrand.LEXUS
        car.model = CarModel.RX350
        car.release_year = ReleaseYear.YEAR_2015
        car.plate_number = "0102"
        car.car_state = CarState.AVAILABLE

        repository.save(car)

        assert repository.find_by_id(car.id) == car

    def test_find_by_id_returns_none(self,session: Session):
        repository = CarRepository(session=session)

        fake_id = uuid.uuid4()

        assert repository.find_by_id(fake_id) is None

    def test_delete_by_id_returns_true(self,session: Session):
        repository = CarRepository(session=session)

        car = Car()
        car.brand = CarBrand.LEXUS
        car.model = CarModel.RX350
        car.release_year = ReleaseYear.YEAR_2012
        car.plate_number = "0103"

        repository.save(car)

        assert repository.count() == 1
        assert repository.delete_by_id(car.id) is True
        assert repository.count() == 0

    def test_delete_non_existent_id_returns_false(self,session: Session) -> None:
        repository = CarRepository(session=session)

        fake_id = (uuid.uuid4())

        assert repository.delete_by_id(fake_id) is False

    def test_save_two_cars_delete_one_count_is_one(self,session: Session):
        repository = CarRepository(session=session)

        car = Car()
        car.brand = CarBrand.LEXUS
        car.model = CarModel.RX350
        car.release_year = ReleaseYear.YEAR_2015
        car.plate_number = "0101"

        repository.save(car)

        car_two = Car()
        car_two.brand = CarBrand.TOYOTA
        car_two.model = CarModel.CAMRY
        car_two.release_year = ReleaseYear.YEAR_2015
        car_two.plate_number = "0102"

        repository.save(car_two)

        repository.delete_by_id(car.id)
        assert repository.count() == 1

    def test_find_by_brand(self,session: Session):
        repository = CarRepository(session=session)

        car = Car()
        car.brand = CarBrand.TOYOTA
        car.model = CarModel.CIVIC
        car.release_year = ReleaseYear.YEAR_2015
        car.plate_number = "0101"

        repository.save(car)

        car_two = Car()
        car_two.brand = CarBrand.TOYOTA
        car_two.model = CarModel.COROLLA
        car_two.release_year = ReleaseYear.YEAR_2015
        car_two.plate_number = "0102"

        repository.save(car_two)

        toyota_cars = repository.find_by_brand(CarBrand.TOYOTA)

        assert len(toyota_cars) == 2