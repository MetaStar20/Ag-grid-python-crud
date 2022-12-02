from typing import List
from sqlalchemy.orm import Session
from exceptions import CarInfoInfoAlreadyExistError, CarInfoNotFoundError
from models import CarInfo
from schemas import CreateAndUpdateCar


# Function to get list of car info
def get_all_cars(session: Session, limit: int, offset: int) -> List[CarInfo]:
    return session.query(CarInfo).offset(offset).limit(limit).all()


# Function to  get info of a particular car
def get_car_info_by_id(session: Session, _id: str) -> CarInfo:
    car_info = session.query(CarInfo).filter(CarInfo.OBJECTID == int(_id)).first()

    if car_info is None:
        raise CarInfoNotFoundError

    return car_info


# Function to add a new car info to the database
def create_car(session: Session, car_info: CreateAndUpdateCar) -> CarInfo:
    car_details = session.query(CarInfo).filter(CarInfo.manufacturer == car_info.manufacturer, CarInfo.modelName == car_info.modelName).first()
    if car_details is not None:
        raise CarInfoInfoAlreadyExistError

    new_car_info = CarInfo(**car_info.dict())
    session.add(new_car_info)
    session.commit()
    session.refresh(new_car_info)
    return new_car_info


# Function to update details of the car
def update_car_info(session: Session, _id: str, info_update: CreateAndUpdateCar) -> CarInfo:
    car_info = get_car_info_by_id(session, _id)

    if car_info is None:
        raise CarInfoNotFoundError

    car_info = info_update

    session.commit()
    session.refresh(car_info)

    return car_info


# Function to delete a car info from the db
def delete_car_info(session: Session, _id: str):
    car_info = get_car_info_by_id(session, _id)

    if car_info is None:
        raise CarInfoNotFoundError

    session.delete(car_info)
    session.commit()

    return