# FastAPI01

Shows examples of using FastAPI

It shows how to set up API endpoints.

This is based on https://fastapi.tiangolo.com/tutorial/

## Running this

To run it:

cd src
uvicorn main:app --reload

Then send HTTP requests to localhost:8000, such as:

http://localhost:8000/

http://localhost:8000/items

http://localhost:8000/items/2

http://localhost:8000/users/me

http://localhost:8000/models/lenet


## Alternative API docs

And now, go to http://127.0.0.1:8000/redoc.
You will see the alternative automatic documentation (provided by ReDoc):
