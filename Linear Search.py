
list = [5,8,4,6,9,2]
n = int(input("Enter the number : \n"))
def search (list,n) :
    i = 0
    while i<len(list) :
        if list[i] == n:
            return True
        i+=1
    return False

if search(list,n) :
    print("Found")
else : print ("Not Found")