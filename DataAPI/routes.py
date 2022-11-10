from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import Any, Dict, AnyStr, List, Union
from models import Book, BookUpdate

router = APIRouter()
JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]


@router.post("/", response_description="Create a new book", status_code=status.HTTP_201_CREATED, response_model=Book)
def create_book(request: Request, book: JSONStructure = None):
    print(book)
    book = jsonable_encoder(book)
    new_book = request.app.database["books"].insert_one(book)
    created_book = request.app.database["books"].find_one(
        {"_id": new_book.inserted_id}
    )

    return created_book


@router.get("/", response_description="List all books", response_model=List[Book])
def list_books(request: Request, _sort: str = "", _order: str = "", _like: str = "", _equal: str = "", _search: str = "", _page: int=0, _limit: int=0):
    if (_sort):
        order = 1
        if (_order == "asc"):
            order = 1
        else:
            order = -1
        books = list(request.app.database["books"].find().sort(_sort, order).skip(_page * 200).limit(_limit))
    elif (_like):
        params = _like.split("__0__")
        print(params)
        books = list(request.app.database["books"].find(
            {params[0]: {'$regex': params[1]}}).limit(_limit))
    elif (_equal):
        params = _equal.split("__0__")
        print(params)
        books = list(request.app.database["books"].find(
            {params[0]:  params[1]}).limit(_limit))
    elif (_search):
        books = list(request.app.database["books"].find({"$or": [{
            "X": _search
        }, {
            "Y": _search
        }, {
            "OBJECTID": _search
        }, {
            "FOLIO": _search
        }, {
            "TTRRSS": _search
        }, {
            "X_COORD": _search
        }, {
            "Y_COORD": _search
        }, {
            "TRUE_SITE_ADDR": _search
        }, {
            "TRUE_SITE_UNIT": _search
        }, {
            "TRUE_SITE_CITY": _search
        }, {
            "TRUE_SITE_ZIP_CODE": _search
        }, {
            "TRUE_MAILING_ADDR1": _search
        }, {
            "TRUE_MAILING_ADDR2": _search
        }, {
            "TRUE_MAILING_ADDR3": _search
        }, {
            "TRUE_MAILING_CITY": _search
        }, {
            "TRUE_MAILING_STATE": _search
        }, {
            "TRUE_MAILING_ZIP_CODE": _search
        }, {
            "TRUE_MAILING_COUNTRY": _search
        }, {
            "TRUE_OWNER1": _search
        }, {
            "TRUE_OWNER2": _search
        }, {
            "TRUE_OWNER3": _search
        }, {
            "CONDO_FLAG": _search
        }, {
            "PARENT_FOLIO": _search
        }, {
            "DOR_CODE_CUR": _search
        }, {
            "DOR_DESC": _search
        }, {
            "SUBDIVISION": _search
        }, {
            "BEDROOM_COUNT": _search
        }, {
            "BATHROOM_COUNT": _search
        }, {
            "HALF_BATHROOM_COUNT": _search
        }, {
            "FLOOR_COUNT": _search
        }, {
            "UNIT_COUNT": _search
        }, {
            "BUILDING_ACTUAL_AREA": _search
        }, {
            "BUILDING_HEATED_AREA": _search
        }, {
            "LOT_SIZE": _search
        }, {
            "YEAR_BUILT": _search
        }, {
            "ASSESSMENT_YEAR_CUR": _search
        }, {
            "ASSESSED_VAL_CUR": _search
        }, {
            "DOS_1": _search
        }, {
            "PRICE_1": _search
        }, {
            "LEGAL": _search
        }, {
            "PID": _search
        }, {
            "DATEOFSALE_UTC": _search
        }]}).limit(_limit))

    else:
        books = list(request.app.database["books"].find().skip(_page * 200).limit(_limit))
    return books


@router.get("/count", response_description="get all items count", response_model=int)
def get_count(request: Request):
  count = request.app.database["books"].count()
  return count

@router.get("/{id}", response_description="Get a single book by id", response_model=Book)
def find_book(id: str, request: Request):
    if (book := request.app.database["books"].find_one({"_id": id})) is not None:
        return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Book with ID {id} not found")


@router.put("/{id}", response_description="Update a book", response_model=Book)
def update_book(id: str, request: Request, book: BookUpdate = Body(...)):
    book = {k: v for k, v in book.dict().items() if v is not None}

    if len(book) >= 1:
        update_result = request.app.database["books"].update_one(
            {"OBJECTID": id}, {"$set": book}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Book with OBJECTID {id} not found")

    if (
        existing_book := request.app.database["books"].find_one({"OBJECTID": id})
    ) is not None:
        return existing_book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Book with OBJECTID {id} not found")


@router.delete("/{id}", response_description="Delete a book")
def delete_book(id: str, request: Request, response: Response):
    delete_result = request.app.database["books"].delete_one({"OBJECTID": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Book with OBJECTID {id} not found")
