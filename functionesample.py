a=10
def sum():
    a = 8
    b = 2
    c = a + b
    return c

# Call sum() and store the result in a variable
d = sum()

def diff():
    a=12
    global x 
    x=4
    y = d - a
    print(y)

# Call diff() with the argument obtained from sum()
diff()
 

