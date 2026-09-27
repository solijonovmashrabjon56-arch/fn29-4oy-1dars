class Movie:
    def init(self, title, genre, year, ticket_price, available_seats):
        self.title = title
        self.genre = genre
        self.year = year
        self.__ticket_price = ticket_price
        self.__available_seats = available_seats

    def buy_ticket(self):
        soni = int(input(f"{self.title} uchun nechta chipta: "))
        if soni <= self.__available_seats:
            self.__available_seats -= soni
            print(f"{soni} ta chipta sotib olindi.")
            print(f"Qolgan joy: {self.__available_seats}")
        else:
            print("Yetarli joy mavjud emas!")

    def add_seats(self, soni):
        self.__available_seats += soni

    def get_info(self):
        print(f"{self.title} ({self.genre}, {self.year})")
        print(f"Narxi: {self.__ticket_price}")
        print(f"Bo'sh joylar: {self.__available_seats}")

    def to_dict(self):
        return {
            "title": self.title,
            "genre": self.genre,
            "year": self.year,
            "ticket_price": self.__ticket_price,
            "available_seats": self.__available_seats
        }

filmlar = [
    Movie("Inception", "Fantastika", 2010, 30000, 30),
    Movie("Titanic", "Drama", 1997, 25000, 20),
    Movie("Interstellar", "Fantastika", 2014, 35000, 25),
    Movie("Joker", "Drama", 2019, 28000, 15),
    Movie("Avatar", "Fantastika", 2009, 32000, 40)
]

while True:
    print("\n1 - Filmlarni ko'rsatish")
    print("2 - Chipta sotib olish")
    print("3 - Joy qo'shish")
    print("4 - Filmni dictionary ko'rinishida ko'rsatish")
    print("0 - Exit")
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        for f in filmlar:
            f.get_info()
    elif tanlov == "2":
        for i, f in enumerate(filmlar):
            print(i, f.title)
        raqam = int(input("Film raqami: "))
        filmlar[raqam].buy_ticket()
    elif tanlov == "3":
        for i, f in enumerate(filmlar):
            print(i, f.title)
        raqam = int(input("Film raqami: "))
        soni = int(input("Qancha joy qo'shiladi: "))
        filmlar[raqam].add_seats(soni)
    elif tanlov == "4":
        for i, f in enumerate(filmlar):
            print(i, f.title)
        raqam = int(input("Film raqami: "))
        print(filmlar[raqam].to_dict())
    elif tanlov == "0":
        break
    else:
        print("Noto'g'ri tanlov!")