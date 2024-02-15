a=["apple","banana","cherry"]
print(type(a))
b=list(a)
print(type(b))
[print(x) for x in b]

b = [x for x in b if "a" in x]  #displays only words within list that contains letter "a"
print(b)

del b[1]
print(b)

b.clear()
print(b)