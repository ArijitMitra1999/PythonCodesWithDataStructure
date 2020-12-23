class A :
    def show(self):
        print("in a show")
#Inheritence
class B(A):
    pass

a1 = B()
a1.show()