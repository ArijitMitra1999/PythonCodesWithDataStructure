from numpy import *

arr1 = array ([
                 [1,2,3,6,8,7],
                 [4,5,6,6,8,7]
             ])
print("It's change 2 dimension to 1 : ",arr1.flatten())
print("Type of Array : ",arr1.dtype)
print("Dimension of Array : ",arr1.ndim)
print("Shape of Array : ",arr1.shape)
print("Size of Array : ",arr1.size)
print("Reshape of Array : \n",arr1.reshape(3,4))
#Matrix
print("**Creating Matrix from Array**")
m = matrix(arr1)
print(m)
#Creating Matrix with out already defined array
print("**New Matrix**")
m = matrix('2 3 4 ; 5 6 7')# using ';' = dimention
print(m)
print(diagonal(m)) #All diagonal values in matrix
print(m.min())