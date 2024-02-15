def sum(x,y):
    a=x+y
    print(a)

sum(2,4)

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly, as shown below:
def children(*kids):  
    print("Youngest Child:" + kids[2])

children("Ajay","Vijay","Anand")

#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
def children(kid2,kid1,kid3):  
    print("Youngest Child:" + kid3)

children(kid1="Ajay",kid2="Vijay",kid3="Anand")

#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:
def children(**kid):  
    print("His last name is :" + kid["lname"] )

children(fname="Ajay",lname="Anand")

#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:
def my_name(name="Ajay"):
    print("My name :" + name)

my_name("Jason")
my_name("Tom")
my_name()
my_name("Vijay")

#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
#E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def marks(scores):
    for x in scores:
     print(x)
points = [55,70,65,77,60]
marks(points)

#To let a function return a value, use the return statement:
def pdt(x):
   return 5 * x

print(pdt(3))
print(pdt(4))
print(pdt(5))