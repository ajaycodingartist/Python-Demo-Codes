class Person:
    def __init__(self,pname,pnage):
        self.name=pname
        self.age=pnage

    def detdisplay(self):
        print("Details of the person :"+self.name,self.age)

class Student(Person):
    def __init__(self,pname,pnage,pyear): 
        super().__init__(pname,pnage)
        self.year=pyear
        
    def print(self):
        print("Details of the person :"+self.name,self.age,self.year)

x=Student("Ajay",24,1997)
print(x.year)
x.detdisplay()
x.print()