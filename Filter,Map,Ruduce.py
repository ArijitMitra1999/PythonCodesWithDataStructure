from functools import *
# def even(n) : return n%2 == 0

num = [2,8,9,12,45,71,32,14,6]

event = list(filter(lambda n :n%2==0,num)) # 'lambda n :n%2==0' =  def even(n) : return n%2 == 0

print("Filter Even Numners: ",event)

double = list(map(lambda n : n+2 , num))

print("Double of num : ",double)

sum = reduce(lambda a,b : a+b ,double)

print(f"Sum of all Double Value : {sum}")


