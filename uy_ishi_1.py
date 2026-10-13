class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

phone = Phone("Samsung", "Galaxy S25 Ultra", 1200)
print(phone.__dict__)

phone.color = "Black"
print(phone.__dict__)
