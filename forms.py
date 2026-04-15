from fastapi import FastAPI, Form
from typing import Annotated, List

app=FastAPI()

L:List=[]

@app.post("/login")
def login(username:Annotated[str, Form()], password:Annotated[str,Form()]):
    L.append(username)
    L.append(password)
    return {"username":username}
    
@app.get("/details")
def get_details():
    return(L[0])