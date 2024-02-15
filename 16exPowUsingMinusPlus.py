def pow():
    a=int(input("Enter Your No. :"))
    b=int(input("Enter the Power :"))
    c=0
    d=0
    for i in range(0,b-1):
        for j in range(0,a):
            c=c+a
        d=d+c
    print(d)
pow()