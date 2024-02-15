class Sum:
    def __init__(self,fnum,snum):
        self.fn=fnum
        self.sn=snum

    def display(self):
        print("Sum is :",self.fn+self.sn)

class Diff:
    def __init__(self,fnum,snum):
        self.fn=fnum
        self.sn=snum

    def display(self):
        print("Difference is :",self.fn-self.sn)

class Pdt:
    def __init__(self,fnum,snum):
        self.fn=fnum
        self.sn=snum

    def display(self):
        print("Product is :",self.fn*self.sn)

class Qnt:
    def __init__(self,fnum,snum):
        self.fn=fnum
        self.sn=snum

    def display(self):
        print("Quotient is :",self.fn/self.sn)

a=Sum(2,4)
b=Diff(4,2)
c=Pdt(5,5)
d=Qnt(24,8)

for x in (a,b,c,d):
    x.display()

