class computer:
    def __init__(self, Name, Colour):
        self.Name = Name
        self.colour = Colour

    def details(self):
        print(f"Name:{self.Name},Colour:{self.colour}")


computer1 = computer("Dell", "Black")
computer2 = computer("Apple", "Grey")

print(computer1.Name)
print(computer2.Name)
computer1.details()
