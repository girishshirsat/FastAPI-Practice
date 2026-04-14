import requests


Items=[
    {"ID":1,"name":"Bag","price":300.00},
    {"ID":2,"name":"Laptop","price":300000.00},
]



responce=requests.post("http://127.0.0.1:8000/items",json=Items)
print(responce.json())

