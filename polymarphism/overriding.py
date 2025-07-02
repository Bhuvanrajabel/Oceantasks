class Flower:
    def Flower(self):
        pass

class Rose(Flower):
    def tell(self):
        return "Pink"

class Sunflower(Flower):
    def tell(self):
        return "Red"
    
flowers=[Rose(),Sunflower()]
for flower in flowers:
    print(flower.tell())
