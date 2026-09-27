class Phone:
    def __init__(self,brand,model,__battary=50):
        self.brand = brand
        self.model = model
        self.__battaty = __battary

    def charge(self):
        self.__battaty += 20
        if self.__battaty > 100:
            self.__battaty = 100

    def usa(self):
        self.__battaty -= 10
        if self.__battaty < 0:
            self.__battaty  = 0

    def get_battary(self):
        return self.__battaty

phone = Phone("IPhone","IPhone 15 pro",87)
print("Batareya: ",phone.get_battary())
phone.charge()
print("Charge: ",phone.get_battary())
phone.usa()
print("Usa: ",phone.get_battary())
i = 0 
while i < 10:
    phone.usa()
    i+=1
print("10 marta use ->",phone.get_battary())