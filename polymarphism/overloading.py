class Calculator:
    def add(self, a, b, c=0):
        if c is not 0:
            return a + b + c
        else:
            return a + b


cal = Calculator()
print(cal.add(5, 10))  
print(cal.add(5, 10, 15))  
