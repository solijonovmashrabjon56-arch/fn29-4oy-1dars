class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.__is_available = True

    def take(self):
        if self.__is_available:
            self.__is_available = False
        else:
            print("Kitob mavjud emas!")

    def return_book(self):
        self.__is_available = True

    def get_info(self):
        print("Nomi:", self.title)
        print("Muallif:", self.author)
        print("Yil:", self.year)
        print("Mavjud:", self.__is_available)

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "is_available": self.__is_available
        }


book = Book("Atomic Habits", "James Clear", 2018)
print(book.to_dict())

book.take()
book.take()
book.return_book()
book.get_info()