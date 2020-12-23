#Instance Varible
#Class Varible

class com :
    SSD = "Fixed"
    def __init__(self):
        #Instance Varible
        self.name = "Dell"
        self.ram = 4
c1 = com()
c2 = com()
c2.name = "HP"
#If I change a single varible like
print(c1.name,c1.ram,c1.SSD)
print(c2.name,c2.ram,c2.SSD)
#We can't change SSD for particular c1 or c2
com.SSD = "Not Fixed"
print(c1.name,c1.ram,c1.SSD)
print(c2.name,c2.ram,c2.SSD)