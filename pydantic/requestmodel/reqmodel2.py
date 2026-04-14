import requests

data=[{"ID":1,"name":"Girish","city":"Nashik","password":"ABC123"},
      {"ID":2,"name":"Dipak","city":"Nashik","password":"ABD123"},
]



resp=requests.post("http://127.0.0.1:8000/send",json=data)

print(resp.json())