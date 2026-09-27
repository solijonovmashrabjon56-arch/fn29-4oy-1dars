class Product:
    def __init__(self,name,price,__quantity):
        self.name = name
        self.price = price
        self.quantity = __quantity
    def add(self,count):
        self.quantity += count

    def sell(self,count):
        if count > self.quantity:
            print("Mahsulot yetarli emas!")
        else:
            self.quantity -= count

    def get_quantity(self):
        return self.quantity

    def get_info(self):
        print("Mahsulot:",self.name)
        print("Narx:",self.price)
        print("Miqdor:",self.quantity)
p = Product("Non",5000,20)
p.get_info()

p.add(10)
print("Miqdor:",p.get_quantity())

p.sell(5)
print("Miqdor:",p.get_quantity())

p.sell(30)