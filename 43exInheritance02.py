class Person:
    def __init__(self,pname,pnage):
        self.name=pname
        self.age=pnage

    def detdisplay(self):
        print("Details of the person :"+self.name,self.age)

class Student(Person):
    def __init__(self,pname,pnage):
        Person.__init__(self,pname,pnage)
        
x=Student("Ajay",24)
x.detdisplay()