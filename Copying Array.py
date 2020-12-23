from numpy import *
#
arr1 = array([2,3,6,4])
#If you just print arr1 = arr2 then it is called shallow copy means address will be same for both
#But if we use .copy() then address willbe changed
arr2 = arr1.copy()

print(arr2)
print("Address of 1st Array : ",id(arr1))
print("Address of 2nd Array : ",id(arr2))