class student :
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    # def sum(self,a,b,c):
    #     s = a + b+ c
    #     return s
    def sum (self,a = None, b = None , c= None) :
        if a != None and b != None and c != None :
            s = a + b + c
        elif a != None and b != None :
            s = a + b
        else : s = a
        return s

s1 = student(23,56)
# print("sum : ",s1.sum(23,56,12))
"""If i pass 2 parameteres but in function we declare 3 paratmeters then"""
print("For Two Parameters : ",s1.sum(12,13))
print("For One Parameter : ",s1.sum(12))
print("For Three Parameters :",s1.sum(12,13,14))