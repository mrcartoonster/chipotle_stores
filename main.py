# -*- coding: utf-8 -*-
from deta import Deta
from environs import Env
from fastapi import FastAPI

env = Env()
env.read_env()
deta = Deta(env("DETA_KEY"))
db = deta.Base("chipotle")

app = FastAPI()


@app.get("/")
def read_root():
    """
    Root file.
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Getting items.
    """
    return {"item_id": item_id}


@app.get("/")
def get_stores():
    """
    Returning all the stores.
    """
    pass
