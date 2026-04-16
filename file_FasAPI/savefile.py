from fastapi import FastAPI,File,UploadFile
from pydantic import BaseModel
from typing import Annotated, List
import os
import shutil

app=FastAPI()

class detail(BaseModel):
    name:str
    content:int

D:List[detail]=[]

@app.post("/upload")
def uploadfile(file:Annotated[UploadFile,File()]):
    D.append(file.filename)
    D.append(file.content_type)
    os.makedirs("upload",exist_ok=True)
    with open(f"upload/{file.filename}","wb") as f :
        shutil.copyfileobj(file.file,f)

    return{"saved file":file.filename}

@app.get("/detail")
def get_saved_file_details():
    return{"name":D[0],"content":D[1]}



