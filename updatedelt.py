from fastapi import FastAPI, HTTPException
from typing import Dict
from pydantic import BaseModel

app=FastAPI()

class student(BaseModel):
    name:str
    mob:int
    city:str


DB:Dict[int,student]={
    1:student(name ="A",mob=75073,city="nashik"),
    2:student(name ="B",mob=73786,city="pune"),
}


@app.post("/add")
def post_student(ID:int,detail:student):
    DB[ID]=detail
    return(DB)

@app.get("/students")
def get_student():
    return DB

@app.put("/update/{ID}")
def update_data(ID:int,detail:student):
    if ID not in DB:
        raise HTTPException(status_code=404, detail="Item not found")
    DB[ID]=detail
    return DB