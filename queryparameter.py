from fastapi import FastAPI


app= FastAPI()

@app.get("/add")
def addition(a:int,b:int):
    return{"addition is":a+b}

@app.get("/items")
def check_type(item:str):
    try:
        item=int(item)
        return{"item is integer":item}
    except ValueError:
        return{"item is string":item}
