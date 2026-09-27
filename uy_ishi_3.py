class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
c = Car("Chevroled","Molibu",2025)
c.color = "Nigga"
print(c.color)
c.color = "White"
print(c.__dict__)