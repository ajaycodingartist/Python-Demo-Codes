a = [1,'Ajay',3.14,True] #ordered, allow duplicates, changable, allows multitype
print(type(a))
print(len(a))
print(a[3])
print(a[1:2])
print(a[-3:-1])
a[1] = 'RDJ' #replacing values
print(a)
a.insert(2,'sss') #insering extra value by replacing using index
print(a)
a.append('AAK') #addin an extra value in the end 
print(a)
b = [2,3,4,5]  #extending another list 'b' into 'a' using extend()
a.extend(b)
print(a)
c = ('Ajay','Anand')
a.extend(c)  #extending a tuple
print(a)
a.remove('Ajay')  # removing an element
print(a)
a.remove(3.14)
print(a) 
a.pop()
print(a)  #pop() to remove the last element
a.pop(2)
print(a) 
del a[3]
print(a)