
# PyMongo with FastAPI CRUD application

This is a simple CRUD application built using PyMongo and FastAPI. You can also follow the step-by-step [tutorial](https://www.mongodb.com/languages/python/pymongo-tutorial) for building this application.

## Running the server

Set your [Atlas URI connection string](https://docs.atlas.mongodb.com/getting-started/) as a parameter in `.env`. Make sure you replace the username and password placeholders with your own credentials.

```
ATLAS_URI=mongodb+srv://<username>:<password>@sandbox.jadwj.mongodb.net (mongodb://localhost:27017/)
DB_NAME=property_point
```

Install the required dependencies:

```
python -m pip install -r requirements.txt
```

Start the server:
```
python -m uvicorn main:app --reload
```

## Running the tests

Install `pytest`:

```
python -m pip install pytest
```

Execute the tests:

```
python -m pytest
```