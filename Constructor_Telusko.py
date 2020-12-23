class computer :
    def __init__(self):
        #Inside the method is instance variable
        self.name = "Arijit"
        self.roll = 65
    def update(self):
        self.roll = 96
    def compare(self,other):
        if self.roll == other.roll  : return True
        else : return False
#Initialize like java
c1 = computer()
c2 = computer()
#Part of Compare
if c1.compare(c2) : print("They are same")
else : print("They are not same")

#Call them
c2.name = "Rohan"
print(c1.name)
print(c2.name)


