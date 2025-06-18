#Basic first code trial code

from pydantic import BaseModel #basemodel class is imported using pydantic library

class rules(BaseModel): #BaseModel class inherited by rule class which helpful to type checking
    
    name:str
    age:int
    


def show_details(name,age):
    
    print(name)
    print(age)
    



person=rules(name="Girish",age=20)#person object of rule class which takes keyword arguments

show_details(person.name,person.age)
