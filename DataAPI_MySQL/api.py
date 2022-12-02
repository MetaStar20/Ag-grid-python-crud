from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from sqlalchemy import or_
from sqlalchemy import desc
from crud import delete_car_info, get_car_info_by_id
from database import get_db
from exceptions import CarInfoException
from schemas import Car, CreateAndUpdateCar

from typing import Any, Dict, AnyStr, List, Union
from models import CarInfo
from fastapi.encoders import jsonable_encoder
import json


router = APIRouter()
JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]

# Example of Class based view


@cbv(router)
class Cars:
    session: Session = Depends(get_db)

    # API to get the list of car info
    @router.get("/")
    def list_cars(self, _sort: str = "", _order: str = "", _like: str = "", _equal: str = "", _search: str = "", _page: int = 0, _limit: int = 0):
        if (_sort):
            if (_order == 'asc'):
                books = self.session.query(CarInfo).order_by(
                    getattr(CarInfo, _sort)).offset(_page * 200).limit(_limit).all()
            else:
                books = self.session.query(CarInfo).order_by(
                    desc(getattr(CarInfo, _sort))).offset(_page * 200).limit(_limit).all()
        elif (_like):
            params = _like.split("__0__")
            print(params)
            search = "%{}%".format(params[1])
            books = self.session.query(CarInfo).filter(getattr(
                CarInfo, params[0]).like(search)).limit(_limit).all()
        elif (_equal):
            params = _equal.split("__0__")
            print(params)
            books = self.session.query(CarInfo).filter(getattr(
                CarInfo, params[0]) == params[1]).limit(_limit).all()
        elif (_search):
            books = self.session.query(CarInfo).filter(
                or_(
                    CarInfo.X.like(_search),
                    CarInfo.Y.like(_search),
                    CarInfo.OBJECTID.like(_search),
                    CarInfo.FOLIO.like(_search),
                    CarInfo.TTRRSS.like(_search),
                    CarInfo.X_COORD.like(_search),
                    CarInfo.Y_COORD.like(_search),
                    CarInfo.TRUE_SITE_ADDR.like(_search),
                    CarInfo.TRUE_SITE_UNIT.like(_search),
                    CarInfo.TRUE_SITE_CITY.like(_search),
                    CarInfo.TRUE_SITE_ZIP_CODE.like(_search),
                    CarInfo.TRUE_MAILING_ADDR1.like(_search),
                    CarInfo.TRUE_MAILING_ADDR2.like(_search),
                    CarInfo.TRUE_MAILING_ADDR3.like(_search),
                    CarInfo.TRUE_MAILING_CITY.like(_search),
                    CarInfo.TRUE_MAILING_STATE.like(_search),
                    CarInfo.TRUE_MAILING_ZIP_CODE.like(_search),
                    CarInfo.TRUE_MAILING_COUNTRY.like(_search),
                    CarInfo.TRUE_OWNER1.like(_search),
                    CarInfo.TRUE_OWNER2.like(_search),
                    CarInfo.TRUE_OWNER3.like(_search),
                    CarInfo.CONDO_FLAG.like(_search),
                    CarInfo.PARENT_FOLIO.like(_search),
                    CarInfo.DOR_CODE_CUR.like(_search),
                    CarInfo.DOR_DESC.like(_search),
                    CarInfo.SUBDIVISION.like(_search),
                    CarInfo.BEDROOM_COUNT.like(_search),
                    CarInfo.BATHROOM_COUNT.like(_search),
                    CarInfo.HALF_BATHROOM_COUNT.like(_search),
                    CarInfo.FLOOR_COUNT.like(_search),
                    CarInfo.UNIT_COUNT.like(_search),
                    CarInfo.BUILDING_ACTUAL_AREA.like(_search),
                    CarInfo.BUILDING_HEATED_AREA.like(_search),
                    CarInfo.LOT_SIZE.like(_search),
                    CarInfo.YEAR_BUILT.like(_search),
                    CarInfo.ASSESSMENT_YEAR_CUR.like(_search),
                    CarInfo.ASSESSED_VAL_CUR.like(_search),
                    CarInfo.DOS_1.like(_search),
                    CarInfo.PRICE_1.like(_search),
                    CarInfo.LEGAL.like(_search),
                    CarInfo.PID.like(_search),
                    CarInfo.DATEOFSALE_UTC.like(_search)

                )
            ).limit(_limit).all()

        else:
            books = list(self.session.query(CarInfo).offset(
                _page * 200).limit(_limit).all())
        books = [u.__dict__ for u in books]
        return books

    # API endpoint to add a car info to the database

    @router.post("/")
    def add_car(self, car_info: JSONStructure = None):
        try:
            obj = jsonable_encoder(car_info)
            new_car_info = CarInfo(**obj)
            self.session.add(new_car_info)
            self.session.commit()
            self.session.refresh(new_car_info)
            return new_car_info
        except CarInfoException as cie:
            raise HTTPException(**cie.__dict__)

    @router.get("/count", response_description="get all items count", response_model=int)
    def get_count(self):
        count = self.session.query(CarInfo).count()
        return count

    # API to update a existing car info
    @router.put("/{id}")
    def update_car(self, id: str, new_info: JSONStructure = None):
        try:
            car_info = get_car_info_by_id(self.session, id)
            obj = jsonable_encoder(new_info)

            car_info.X = obj['X']
            car_info.Y = obj['Y']
            car_info.OBJECTID = obj['OBJECTID']
            car_info.FOLIO = obj['FOLIO']
            car_info.TTRRSS = obj['TTRRSS']
            car_info.X_COORD = obj['X_COORD']
            car_info.Y_COORD = obj['Y_COORD']
            car_info.TRUE_SITE_ADDR = obj['TRUE_SITE_ADDR']
            car_info.TRUE_SITE_UNIT = obj['TRUE_SITE_UNIT']
            car_info.TRUE_SITE_CITY = obj['TRUE_SITE_CITY']
            car_info.TRUE_SITE_ZIP_CODE = obj['TRUE_SITE_ZIP_CODE']
            car_info.TRUE_MAILING_ADDR1 = obj['TRUE_MAILING_ADDR1']
            car_info.TRUE_MAILING_ADDR2 = obj['TRUE_MAILING_ADDR2']
            car_info.TRUE_MAILING_ADDR3 = obj['TRUE_MAILING_ADDR3']
            car_info.TRUE_MAILING_CITY = obj['TRUE_MAILING_CITY']
            car_info.TRUE_MAILING_STATE = obj['TRUE_MAILING_STATE']
            car_info.TRUE_MAILING_ZIP_CODE = obj['TRUE_MAILING_ZIP_CODE']
            car_info.TRUE_MAILING_COUNTRY = obj['TRUE_MAILING_COUNTRY']
            car_info.TRUE_OWNER1 = obj['TRUE_OWNER1']
            car_info.TRUE_OWNER2 = obj['TRUE_OWNER2']
            car_info.TRUE_OWNER3 = obj['TRUE_OWNER3']
            car_info.CONDO_FLAG = obj['CONDO_FLAG']
            car_info.PARENT_FOLIO = obj['PARENT_FOLIO']
            car_info.DOR_CODE_CUR = obj['DOR_CODE_CUR']
            car_info.DOR_DESC = obj['DOR_DESC']
            car_info.SUBDIVISION = obj['SUBDIVISION']
            car_info.BEDROOM_COUNT = obj['BEDROOM_COUNT']
            car_info.BATHROOM_COUNT = obj['BATHROOM_COUNT']
            car_info.HALF_BATHROOM_COUNT = obj['HALF_BATHROOM_COUNT']
            car_info.FLOOR_COUNT = obj['FLOOR_COUNT']
            car_info.UNIT_COUNT = obj['UNIT_COUNT']
            car_info.BUILDING_ACTUAL_AREA = obj['BUILDING_ACTUAL_AREA']
            car_info.BUILDING_HEATED_AREA = obj['BUILDING_HEATED_AREA']
            car_info.LOT_SIZE = obj['LOT_SIZE']
            car_info.YEAR_BUILT = obj['YEAR_BUILT']
            car_info.ASSESSMENT_YEAR_CUR = obj['ASSESSMENT_YEAR_CUR']
            car_info.ASSESSED_VAL_CUR = obj['ASSESSED_VAL_CUR']
            car_info.DOS_1 = obj['DOS_1']
            car_info.PRICE_1 = obj['PRICE_1']
            car_info.LEGAL = obj['LEGAL']
            car_info.PID = obj['PID']
            car_info.DATEOFSALE_UTC = obj['DATEOFSALE_UTC']

            self.session.commit()
            self.session.refresh(car_info)
            return car_info
        except CarInfoException as cie:
            raise HTTPException(**cie.__dict__)

    # API to delete a car info from the data base

    @router.delete("/{id}")
    def delete_car(self, id: str):
        try:
            return delete_car_info(self.session, id)
        except CarInfoException as cie:
            raise HTTPException(**cie.__dict__)
