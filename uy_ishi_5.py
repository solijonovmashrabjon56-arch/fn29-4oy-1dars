class Car:
    def __init__(self,brand,model,year,speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerste(self):
        self.speed += 20

    def brake(self):
        if self.speed >= 20:
            self.speed -=20

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}),tezlik: {self.speed}"

car = Car("Chevroled","cobalt",2022)
print("Tezlik:",car.speed)

car.accelerste()
print("Accelerate ->",car.speed)

car.accelerste()
print("Accelerate ->",car.speed)

car.brake()
print("Brake ->",car.speed)

print(car.get_info())