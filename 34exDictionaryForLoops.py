a={"Brand" : "Ford", "Model" : "Mustang", "Year" : 1964}
print(a)

#2 methods for displaying values only given below

for i in a:
    print(i)

for i in a.keys():  #for displaying keys only
    print(i)

#2 methods for displaying values only given below

for i in a:  #for displaying values only
    print(a[i])

for i in a.values(): #for displaying values only
    print(i)

b=a.copy()
print(b)

c=dict(a)
print(c)

