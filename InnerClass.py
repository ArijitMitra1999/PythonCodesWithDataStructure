class Student :

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        #Inner class declared
        self.lap = self.Laptop()
    def show(self):
        print(self.name,self.roll)
        #Inner class called
        self.lap.show()
    #Inner Class
    class Laptop :
        def __init__(self):
            self.brand = "hp"
            self.cpu ='i5'
            self.ram = 8
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student("Arijit",24)
s2 = Student("Prayash",16)

s1.show()
