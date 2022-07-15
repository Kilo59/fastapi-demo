from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Demo API",
    docs_url="/",
    redoc_url="/docs",
    version="1.0.0",
)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/items", response_model=list[Item])
def list_items():
    pass


@app.post("/items", response_model=Item)
def create_item(item: Item):
    pass


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    pass


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    pass
