def Generators() :
    n = 1
    while n<=10 :
        yield n
        n += 1
values = Generators()
# print(values.__next__())
for i in values :
    print(i)

"""
* Difference between yield and return *

return sends a specified value back to its caller, whereas yield can produce a sequence of values. 
We should use yield when we want to iterate over a sequence but don't want to store the entire sequence in memory. 
yield is used in Python generators.
"""