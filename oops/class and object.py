class fruits:
    def __init__(self,Name,Price):
        self.Name = Name
        self.Price = Price

    def details(self):
        print(f"Name:{self.Name},price:{self.Price}")

fruits1=fruits("banana",21)
fruits2=fruits("Apple",10)

print(fruits1.Name)
print(fruits2.Price)
fruits1.details()

