from fastapi import FastAPI

app=FastAPI()

@app.get("/itemsint/{items_id}")
def read_item(items_id:int):
    return {"item is integer":items_id}

@app.get("/itemsfloat/{items_id}")
def read_item(items_id:float):
    return {"item is float":items_id}

@app.get("/itemsstr/{items_id}")
def read_item(items_id:str):
    return {"item is string":items_id}