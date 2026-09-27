class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
b1 = Book("O'tgan kunlar","Abdulla Qodri",1926)
b1.price = 70000
b1.price = 65.900
print(b1.price)
b1.year = 1930
del b1.price
print(b1.__dict__)