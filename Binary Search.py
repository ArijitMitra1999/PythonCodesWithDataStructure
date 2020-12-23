list1 = [5,8,48,65,9]
n = 48

def search (list1,n) :
    l = 0
    u = len(list1) - 1
    while l <= u :
        mid = l+u // 2
        if list1(mid) == n :
            return True
        else :
            if list1(mid) < n :
                l = mid + 1
            else :
                u =  mid - 1
    return False

if search(list1, n):
    print("Found")
else :
    print ("Not Found")