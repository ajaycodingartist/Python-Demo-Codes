class Person:
    # def __init__(self,pname,pnage):
    #     self.name=pname
    #     self.age=pnage

    def detdisplay(self,a,b):
        name=a
        age=b
        print("Details of the person :"+name,age)

    def add(self,x,y):
        e=x
        t=y
        print("Sum is:",e+t)

# class Student(Person):
#     pass

z=Person()
l=Person()
z.detdisplay("John",26)
l.detdisplay("Ram",27)
z.add(4,6)

# x=Student("Ajay",24)
# x.detdisplay()