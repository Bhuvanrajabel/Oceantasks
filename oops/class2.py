class freefire:
    def __init__(self, Name, Bundle):
        self.Name = Name
        self.Bundle = Bundle

    def details(self):
        print(f"Name:{self.Name},Bundle:{self.Bundle}")


freefire1 = freefire("Bhuvan2711", "Joker")
freefire2 = freefire("BS Captain", "criminal")

print(freefire1.Name)
print(freefire2.Name)
freefire1.details()
