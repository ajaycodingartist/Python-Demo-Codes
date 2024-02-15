a={"Brand" : "Ford", "Model" : "Mustang", "Year" : 1964}
print(a)

if "Model" in a:
    print("Yes Model present in the key lists")

a["Year"] = 1980  #updating without update() 
print(a)

a.update({"Type" : "Racing"})  #adding new elements using update()
print(a)

a["Colour"] = ["Matte Navy Blue", "Matte Black"] #any datatypes can be added into the dictionaries
print(a)

a.pop("Type")  #we can decide which element should be poped or deleted
print(a)

a.popitem()  #automatically the last item will be deleted
print(a)

del a["Year"]
print(a)

a.clear()
print(a)