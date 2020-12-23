from array import *
arr = array ('i',[])
n = int(input("Enter the length : "))
for i in range (n):
    x = int(input("Enter the value : \n"))
    arr.append(x)
print(arr)

#Searching Array
k = 0
val = int(input("Enter the number you search : "))
# for i in arr :
#     if i == val :
#         print(k)
#         break
#     k += 1
print(arr.index(val)) #Find Index