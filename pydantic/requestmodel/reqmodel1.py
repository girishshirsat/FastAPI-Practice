from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
class student(BaseModel):
    ID:int
    name:str
    city:str|None
    password:str

class ResponceIn(BaseModel):
    ID:int
    name:str
    city:str|None
    password:str

class ResponceOut(BaseModel):
    ID:int
    name:str
    city:str|None
   

app=FastAPI()

students:List[student]=[]

@app.post("/send",response_model=List[ResponceOut])
def send_data(data:List[ResponceIn]):
    students.clear()
    students.extend(data)
    return data

@app.get("/take",response_model=List[ResponceOut])
def take_data():
    return students
