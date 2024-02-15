class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Destroying the object {self.name}")

# Creating an instance of the class
obj = MyClass("Example")

# Deleting the object explicitly
del obj 
 