from fastapi import FastAPI, File, UploadFile
from typing import Annotated, List
from pydantic import BaseModel


app=FastAPI()


class filedetail(BaseModel):
    name:str
    content:str
    length:int

D:List[filedetail]=[]

@app.post("/size")
def upload(file:Annotated[bytes,File()]):
    D.append(len(file))
    return{"File size":len(file)}

@app.post("/name")
def file_name(file:Annotated[UploadFile, File()]):
    D.append(file.filename)
    D.append(file.content_type)
    return{"Filename":file.filename,"Content":file.content_type}

@app.get("/details")
def get_details():
    return{"name":D[1],"Content":D[2],"Size":D[0]}