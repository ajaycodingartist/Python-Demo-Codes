#Simplest form of class
class Myclass:
    x=5+6

p=Myclass()
print(p.x)

#The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
#To understand the meaning of classes we have to understand the built-in __init__() function.
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Details:
    def __init__(self, name, age):
        self.name=name
        self.age=age

d=Details("Ajay",24)
print(d.name)
print(d.age)

#The __str__() function controls what should be returned when the class object is represented as a string.
#If the __str__() function is not set, the string representation of the object is returned:
class Details:
    def __init__(self, name, age, phone):
        self.name=name
        self.age=age
        self.phone=phone
    
    def __str__(self):
        return f"{self.name}({self.age})[{self.phone}]"

d=Details("Ajay",24,9048860126)
print(d)

#Objects can also contain methods. Methods in objects are functions that belong to the object.
#Let us create a method in the Person class:

class Details:
    def __init__(self, name, age, phone):
        self.name=name
        self.age=age
        self.phone=phone
    
    def personal(self):
        print("Name of the person :"+self.name) 

d=Details("Ajay",24,9048860126)
d.age=25
print(d.age)  #You can modify properties on objects like this
d.personal()
