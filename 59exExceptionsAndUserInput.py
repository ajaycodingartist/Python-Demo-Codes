try:
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    x=a/b
except:
    print("Undefined")
else:
    print("The no. is :",x)
finally:
    print("Task Completed")