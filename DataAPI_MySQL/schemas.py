from pydantic import BaseModel
from typing import Optional, List


# TO support creation and update APIs
class CreateAndUpdateCar(BaseModel):
    X:  str
    Y:  str
    OBJECTID: int
    FOLIO: str
    TTRRSS: str
    X_COORD: str
    Y_COORD: str
    TRUE_SITE_ADDR: str
    TRUE_SITE_UNIT: str
    TRUE_SITE_CITY: str
    TRUE_SITE_ZIP_CODE: str
    TRUE_MAILING_ADDR1: str
    TRUE_MAILING_ADDR2: str
    TRUE_MAILING_ADDR3: str
    TRUE_MAILING_CITY: str
    TRUE_MAILING_STATE: str
    TRUE_MAILING_ZIP_CODE: str
    TRUE_MAILING_COUNTRY: str
    TRUE_OWNER1: str
    TRUE_OWNER2: str
    TRUE_OWNER3: str
    CONDO_FLAG: str
    PARENT_FOLIO: str
    DOR_CODE_CUR: str
    DOR_DESC: str
    SUBDIVISION: str
    BEDROOM_COUNT: str
    BATHROOM_COUNT: str
    HALF_BATHROOM_COUNT: str
    FLOOR_COUNT: str
    UNIT_COUNT: str
    BUILDING_ACTUAL_AREA: str
    BUILDING_HEATED_AREA: str
    LOT_SIZE: str
    YEAR_BUILT: str
    ASSESSMENT_YEAR_CUR: str
    ASSESSED_VAL_CUR: str
    DOS_1: str
    PRICE_1: str
    LEGAL: str
    PID: str
    DATEOFSALE_UTC: str


# TO support list and get APIs
class Car(CreateAndUpdateCar):
    id: int

    class Config:
        orm_mode = True

# To support list cars API
class PaginatedCarInfo(BaseModel):
    limit: int
    offset: int
    data: List[Car]

