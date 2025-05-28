#square of a number
def square(num):
    return num*num 
numbers=[1,2,3,4,5,6,7]
square=map(square,numbers)
print(list(square))


#check if elements are even using lambda
numbers = [1, 2, 3, 4, 5, 6]
even_check = list(map(lambda x: x % 2 == 0, numbers))
print(even_check)

#
words = ["jadeja", "rahul", "dhoni"]
capitalized = list(map(lambda w: w.title(), words))
print(capitalized)


#string no to integer
a= ['1', '2', '3', '4']
b= list(map(int, a))
print(b)

# reverse a string 
words = ["lokesh", "oliver", "christiano"]
reversed_words = list(map(lambda w: w[::-1], words))
print(reversed_words)

#uppercase
def up(a):
    return a.upper()
m = ["ramesh","ashwin"]
b = map(up, m)
print(list(b))