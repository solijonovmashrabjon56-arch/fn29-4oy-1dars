class SmartDevice:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self._status = False

    def turn_on(self):
        self._status = True

    def turn_off(self):
        self._status = False

    def get_status(self):
        holat = "yoqilgan" if self._status else "o'chirilgan"
        print(f"{self.name} ({self.room}) - {holat}")

    def to_dict(self):
        return {
            "name": self.name,
            "room": self.room,
            "status": self._status
        }


qurilmalar = [
    SmartDevice("Lamp", "Yotoqxona"),
    SmartDevice("TV", "Mehmonxona"),
    SmartDevice("Konditsioner", "Xona"),
    SmartDevice("Ventilyator", "Oshxona")
]

while True:
    print("\n1 - Barcha qurilmalarni ko'rsatish")
    print("2 - Qurilmani yoqish")
    print("3 - Qurilmani o'chirish")
    print("4 - Dictionary ko'rinishida chiqarish")
    print("0 - Exit")
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        for q in qurilmalar:
            q.get_status()
    elif tanlov == "2":
        for i, q in enumerate(qurilmalar):
            print(i, q.name)
        raqam = int(input("Qurilma raqami: "))
        qurilmalar[raqam].turn_on()
    elif tanlov == "3":
        for i, q in enumerate(qurilmalar):
            print(i, q.name)
        raqam = int(input("Qurilma raqami: "))
        qurilmalar[raqam].turn_off()
    elif tanlov == "4":
        for q in qurilmalar:
            print(q.to_dict())
    elif tanlov == "0":
        print("Dastur tugadi")
        break
    else:
        print("Noto'g'ri tanlov!")