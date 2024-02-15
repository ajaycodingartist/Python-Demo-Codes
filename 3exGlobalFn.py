#global variable
a=4
b=2
def display():
    a=5        #local variable
    print("value of a",a)
    
def result():
    global b   #global defined inside function
    b=8
    a=10
    print("value of b",b)

display()#calling local var a=5

print("value of global a",a)#calling global var a=4

result()#calling global var b=8 which is defined inside function

print(b)#here global variable updated as from b=2 to b=8