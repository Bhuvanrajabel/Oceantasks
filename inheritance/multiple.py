class Father:
    def skill(self):
        print("Master")

class Mother:
    def tricks(self):
        print("Grandmaster")

class Child(Father,Mother):
    pass

a=Child()
a.skill()
a.tricks()