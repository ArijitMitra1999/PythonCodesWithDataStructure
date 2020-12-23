def getdate():
    import datetime
    return datetime.datetime.now() #using now() to get current time
n = int(input("Enter the Number : "))
for i in range (2,n) :
    if(n%i == 0) :
        print (str(str(getdate())),":" ,"Not a prime number")
        break
else :
    print("Prime Number")
#That is how for else loop works