class Computer:
    device_type = "Computer"
    def __init__(self,brand,ram,storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage
computer1 = Computer("acer",16,1024)
computer2 = Computer("lenovo",8,256)
print(Computer.device_type)
print(computer1.device_type)
print(computer2.device_type)

computer1.device_type = "Loptop"

print(computer1.device_type)
print(computer2.device_type)
print(Computer.device_type)

print(computer1.__dict__)
print(computer2.__dict__)