import uuid
from typing import Optional
from pydantic import BaseModel, Field
from typing import Union

class Book(BaseModel):
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    X:  Union[str, None] = None 
    Y:  Union[str, None] = None 
    OBJECTID: Union[str, None] = None 
    FOLIO: Union[str, None] = None 
    TTRRSS: Union[str, None] = None 
    X_COORD: Union[str, None] = None 
    Y_COORD: Union[str, None] = None 
    TRUE_SITE_ADDR: Union[str, None] = None 
    TRUE_SITE_UNIT: Union[str, None] = None 
    TRUE_SITE_CITY: Union[str, None] = None 
    TRUE_SITE_ZIP_CODE: Union[str, None] = None 
    TRUE_MAILING_ADDR1: Union[str, None] = None 
    TRUE_MAILING_ADDR2: Union[str, None] = None 
    TRUE_MAILING_ADDR3: Union[str, None] = None 
    TRUE_MAILING_CITY: Union[str, None] = None 
    TRUE_MAILING_STATE: Union[str, None] = None 
    TRUE_MAILING_ZIP_CODE: Union[str, None] = None 
    TRUE_MAILING_COUNTRY: Union[str, None] = None 
    TRUE_OWNER1: Union[str, None] = None 
    TRUE_OWNER2: Union[str, None] = None 
    TRUE_OWNER3: Union[str, None] = None 
    CONDO_FLAG: Union[str, None] = None 
    PARENT_FOLIO: Union[str, None] = None 
    DOR_CODE_CUR: Union[str, None] = None 
    DOR_DESC: Union[str, None] = None 
    SUBDIVISION: Union[str, None] = None 
    BEDROOM_COUNT: Union[str, None] = None 
    BATHROOM_COUNT: Union[str, None] = None 
    HALF_BATHROOM_COUNT: Union[str, None] = None 
    FLOOR_COUNT: Union[str, None] = None 
    UNIT_COUNT: Union[str, None] = None 
    BUILDING_ACTUAL_AREA: Union[str, None] = None 
    BUILDING_HEATED_AREA: Union[str, None] = None 
    LOT_SIZE: Union[str, None] = None 
    YEAR_BUILT: Union[str, None] = None 
    ASSESSMENT_YEAR_CUR: Union[str, None] = None 
    ASSESSED_VAL_CUR: Union[str, None] = None 
    DOS_1: Union[str, None] = None 
    PRICE_1: Union[str, None] = None 
    LEGAL: Union[str, None] = None 
    PID: Union[str, None] = None 
    DATEOFSALE_UTC: Union[str, None] = None 

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "X": "-80.1929511084272",
                "Y": "25.7722413121729",
                "OBJECTID": "1",
                "FOLIO": "0101000000020",
                "TTRRSS": "544101",
                "X_COORD": "921757.4",
                "Y_COORD": "523723.3",
                "TRUE_SITE_ADDR": "",
                "TRUE_SITE_UNIT": "",
                "TRUE_SITE_CITY": "Miami",
                "TRUE_SITE_ZIP_CODE": "33131-2103",
                "TRUE_MAILING_ADDR1": "1000 BRICKELL AVE STE 400",
                "TRUE_MAILING_ADDR2": "",
                "TRUE_MAILING_ADDR3": "",
                "TRUE_MAILING_CITY": "MIAMI",
                "TRUE_MAILING_STATE": "FL",
                "TRUE_MAILING_ZIP_CODE": "33131",
                "TRUE_MAILING_COUNTRY": "USA",
                "TRUE_OWNER1": "16 SE 2ND STREET DOWNTOWN",
                "TRUE_OWNER2": "INVESTMENT LLC",
                "TRUE_OWNER3": "",
                "CONDO_FLAG": "N",
                "PARENT_FOLIO": "",
                "DOR_CODE_CUR": "2865",
                "DOR_DESC": "PARKING LOT/MOBILE HOME PARK : PARKING LOT",
                "SUBDIVISION": "010100000",
                "BEDROOM_COUNT": "0",
                "BATHROOM_COUNT": "0",
                "HALF_BATHROOM_COUNT": "0",
                "FLOOR_COUNT": "0",
                "UNIT_COUNT": "0",
                "BUILDING_ACTUAL_AREA": "0",
                "BUILDING_HEATED_AREA": "0",
                "LOT_SIZE": "60198",
                "YEAR_BUILT": "0",
                "ASSESSMENT_YEAR_CUR": "2023",
                "ASSESSED_VAL_CUR": "39135489",
                "DOS_1": "20210623",
                "PRICE_1": "46000000",
                "LEGAL": "MIAMI NORTH PB B-41 BEG X OF E/L OF SO MIAMI AVE & S/L SE 2 DT TH E350FT S149FT W139.76FT S55.32FT N 84 DEG W126.02FT NWLY A/D 49.35FT N 81 DEG W13.92FT N 8 DEG E38.75FT W61FT N125.12FT TO POB LOT SIZE 60198 SQ FT COC 25843-0025 26307-3840 0707 6",
                "PID": "538415",
                "DATEOFSALE_UTC": "2021/06/23 04:00:00+00"
            }
        }


class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    synopsis: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "X": "-80.1929511084272",
                "Y": "25.7722413121729",
                "FOLIO": "0101000000020",
                "TTRRSS": "544101",
                "X_COORD": "921757.4",
                "Y_COORD": "523723.3",
                "TRUE_SITE_ADDR": "",
                "TRUE_SITE_UNIT": "",
                "TRUE_SITE_CITY": "Miami",
                "TRUE_SITE_ZIP_CODE": "33131-2103",
                "TRUE_MAILING_ADDR1": "1000 BRICKELL AVE STE 400",
                "TRUE_MAILING_ADDR2": "",
                "TRUE_MAILING_ADDR3": "",
                "TRUE_MAILING_CITY": "MIAMI",
                "TRUE_MAILING_STATE": "FL",
                "TRUE_MAILING_ZIP_CODE": "33131",
                "TRUE_MAILING_COUNTRY": "USA",
                "TRUE_OWNER1": "16 SE 2ND STREET DOWNTOWN",
                "TRUE_OWNER2": "INVESTMENT LLC",
                "TRUE_OWNER3": "",
                "CONDO_FLAG": "N",
                "PARENT_FOLIO": "",
                "DOR_CODE_CUR": "2865",
                "DOR_DESC": "PARKING LOT/MOBILE HOME PARK : PARKING LOT",
                "SUBDIVISION": "010100000",
                "BEDROOM_COUNT": "0",
                "BATHROOM_COUNT": "0",
                "HALF_BATHROOM_COUNT": "0",
                "FLOOR_COUNT": "0",
                "UNIT_COUNT": "0",
                "BUILDING_ACTUAL_AREA": "0",
                "BUILDING_HEATED_AREA": "0",
                "LOT_SIZE": "60198",
                "YEAR_BUILT": "0",
                "ASSESSMENT_YEAR_CUR": "2023",
                "ASSESSED_VAL_CUR": "39135489",
                "DOS_1": "20210623",
                "PRICE_1": "46000000",
                "LEGAL": "MIAMI NORTH PB B-41 BEG X OF E/L OF SO MIAMI AVE & S/L SE 2 DT TH E350FT S149FT W139.76FT S55.32FT N 84 DEG W126.02FT NWLY A/D 49.35FT N 81 DEG W13.92FT N 8 DEG E38.75FT W61FT N125.12FT TO POB LOT SIZE 60198 SQ FT COC 25843-0025 26307-3840 0707 6",
                "PID": "538415",
                "DATEOFSALE_UTC": "2021/06/23 04:00:00+00"
            }
        }
