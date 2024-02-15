import numpy as np

x=np.array([11,12,13,14,15])  #1D arrays

print("1st Example:",x)
print("4th element is:",x[3])
print("Sum of 1st and 4th elements:",x[1]+x[3])  #add values of the given index
print(type(x))

y=np.array([[1,2,3,4,5],[6,7,8,9,10]])  #2D arrays
print("2nd Example:",y)
print("3rd element in 1st row:",y[0,2])
print("Sum of 2nd element in 1st row and 5th element in 2nd row:",y[0,1]+y[1,4])  #add values of the given index

z=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])  #3D arrays
print(z)
print("Display 1st element in 2nd array in 2nd row:",z[1,1,0])
print("Sum of 1st element in 2nd array in 1st row and 3rd element in 1st array in 2nd row:",z[0,1,0]+z[1,0,2])  #add values of the given index
