class car():
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def describe(self):
        print(self.year,self.brand,self.model)
    
A=car("Toyota","Camry",2020)
A.describe()
B=car("Maruti","maruti800",2015)
B.describe()
