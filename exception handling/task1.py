# safe division function
# def function(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "Error cannot divide by zero"
# print(function(10,0))


# convert string into integers
def function (a):
    try:
        print(int(a))
    except ValueError:
        print (0)
function("harry potter")


# Parse float
# def parse_float(s):
#     try:
#         return float(s)
#     except ValueError:
#         return "Invalid float"
# print(parse_float("abc"))

# sum of the elements
# def sum_list(a):
#     try:
#         return sum(a)
#     except TypeError:
#         return "List contains non-numeric data"
# print(sum_list([1, 'a', 3]))


# multiple numbers
# def function(a, b):
#     try:
#         return a * b
#     except TypeError:
#         return "Invalid types for multiplication"
# print(function(5, 3))

# using uppercase
# def uppercase(a):
#     try:
#         return a.upper()
#     except AttributeError:
#         return "Input is not a string"
# print(uppercase("hello"))

# reading integer from user
# def integer(prompt):
#     try:
#         return int(input(prompt))
#     except ValueError:
#         return "Invalid integer"
# print(integer("Enter a number: "))


#elements by index
# def get_element(lst, index):
#     try:
#         return lst[index]
#     except IndexError:
#         return "Index out of range"
# print(get_element([1, 2, 3], 1))
