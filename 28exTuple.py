a=(1,2,3,4,5,6)
print(type(a))
b=list(a)
print(type(b))  #converted a tuple into list
print(b)

print(len(b))

b[1:3] = [9,8,7,6,]

b.append(2)
print(b)

b.insert(2,'Ajay')
print(b)

c=(8,9)
d=list(c)
b.extend(d) 
print(b)

b.remove('Ajay')
print(b)

b.pop()
print(b)

b.sort()
print(b)

i=0
while(i<len(b)):
    print(b[i])
    i=i+1
