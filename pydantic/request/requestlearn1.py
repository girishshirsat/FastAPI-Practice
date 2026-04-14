from pydantic import BaseModel
from fastapi import FastAPI
from typing import List

app = FastAPI()



class Item(BaseModel):
    ID: int
    name: str
    price: float


itemlist:List[Item]=[]

@app.post("/items")
def createitems(items: list[Item]):
    itemlist.clear()
    itemlist.extend(items)  # ← List of items
    return items


# from requestlearn2 import responce



@app.get("/itemlist")
def get_itemlist():
    return itemlist

