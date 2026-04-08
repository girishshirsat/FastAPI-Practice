from fastapi import FastAPI

app=FastAPI()

@app.get("itemsint/{items_id}")
def read_item(item_id:int):
    return {"item is integer":item_id}

@app.get("itemsfloat/{items_id}")
def read_item(item_id:float):
    return {"item is float":item_id}

@app.get("itemsstr/{items_id}")
def read_item(item_id:str):
    return {"item is string":item_id}