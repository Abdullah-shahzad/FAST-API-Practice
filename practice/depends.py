from typing import Annotated
from fastapi import Depends, FastAPI
from dependencies import common_parameters
app = FastAPI()

c = Annotated[dict, Depends(common_parameters)]

@app.get("/items/")
async def read_items(commons: c):
    return commons

@app.get("/users/")
async def read_users(commons: c):
    return commons['q']

