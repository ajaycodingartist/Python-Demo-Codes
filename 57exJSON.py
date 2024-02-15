import json

x='{"name":"Ajay","age":24,"city":"Kochi"}'
a={"name":"Steve","age":30,"city":"Brooklyn"}
y=json.loads(x)  #converting JSON to Python
b=json.dumps(a)  #converting Python to JSON

print(y)
print(b)

# JSON is a syntax for storing and exchanging data, to convert input data into programming language strings.
# JSON is text, written with JavaScript object notation.
# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent.