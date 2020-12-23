from functools import wraps
def div (a,b) :
    print(a/b)

def smart_div (func) :
    wraps(func)
    def inner(a,b) :
        if a<b :
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)

div(2,4)
#Decorate a function