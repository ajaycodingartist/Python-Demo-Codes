x=300 #Global variable

def Myfun():
    x=200  #Local variable
    print("The Local variable:",x)

Myfun()

print("The Global variable:",x)