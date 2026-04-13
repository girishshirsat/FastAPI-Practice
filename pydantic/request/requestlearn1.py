from pydantic import BaseModel
from fastapi import FastAPI
from typing import List

app = FastAPI()

class Item(BaseModel):
    ID: int
    name: str
    price: float

@app.post("/items")
def createitems(items: List[Item]):  # ← List of items
    return items