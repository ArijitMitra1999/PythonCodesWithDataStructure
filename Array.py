from array import *

vals = array('i',[5,6,7,9,6])

for i in range (len(vals)) :
    print(i)
print("Type of this code :",vals.typecode) #print Type of this code

"""Create New Array from new Array"""

newarr = [array(vals.typecode,(a for a in vals ))]

for e in newarr :
    print(e , end = " ")