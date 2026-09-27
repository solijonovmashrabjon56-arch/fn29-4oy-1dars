class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
phone = Phone("IPhone","IPhone 15 pro",7500)
print(phone.__dict__)
phone.color = "Titanium"
print(phone.__dict__)