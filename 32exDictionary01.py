thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

a={"Brand" : "Ford", "Model" : "Mustang", "Year" : 1964}
print(a) 

#above given 2 ways of representing dictionaries
 
x=a.get("Model")  #displays the item in given label
print(x) 

y=a.keys()  #displays the labels of the given dictionary
print(y)

z=a.values()  #displays the values/items of the given dictionary
print(z)

t=a.items()  #groups and displays the labels and the corresponding values/items of the given dictionary
print(t)

a.update({"Model" : "Renault"})
print(a)

a["Type"] = "Racing"  #adding extra label and value 
print(a)

a["Colour"] = ["Matte Navy Blue", "Matte Black"] #any datatypes can be added into the dictionaries
print(a)

