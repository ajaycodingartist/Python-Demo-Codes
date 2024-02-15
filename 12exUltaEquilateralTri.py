def star():
    t=10
    for i in range(0,t):
        for j in range(0,i):
            print(end=" ")
        for k in range(0,t-i):
            print("*",end=" ")
        print("\r")

star()