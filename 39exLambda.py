#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5,6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def twice(n):
    return lambda a: a * n    #x=lambda a: a*n
x = twice(2)
print(x(10))

def thrice(n):
    return lambda a: a * n
x = thrice(3)
print(x(10))

def myfun(n):
    print("Both doubling and trippling")
    return lambda a: a * n
doubler = myfun(2)
trippler = myfun(3)
print(doubler(10))
print(trippler(10))