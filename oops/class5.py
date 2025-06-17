class students:
    def __init__(self, Name, Colour,Age):
        self.Name = Name
        self.colour = Colour
        self.Age = Age

    def details(self):
        print(f"Name:{self.Name},Colour:{self.colour},Age:{self.Age}")


students1 = students("Nathan", "White",32)
students2 = students("Kamalesh", "Black",90)

print(students1.Name)
print(students2.Age)
students2.details()
