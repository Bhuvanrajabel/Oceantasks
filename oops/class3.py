class colour:
    def __init__(self, Name, colour):
        self.Name = Name
        self.colour = colour

    def details(self):
        print(f"Name:{self.Name},:{self.colour}")

colour1 = colour("Apple", "Red")
colour2 = colour("Banana", "Yellow")

print(colour2.Name)
print(colour1.Name)
colour1.details()
