def myfunction(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper
@myfunction
def say_hello():
    a=20
    b=50
    print(a+b)
say_hello()