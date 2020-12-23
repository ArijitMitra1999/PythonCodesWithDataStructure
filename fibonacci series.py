def fibonacci(n):
    a = 0
    b = 1
    if n <= 0: print("Incorrect input")
    elif n == 1: return a
    else:
        print (a,b,end = " ")
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c , end= " ")

print(fibonacci(int(input("Enter the Number : "))))