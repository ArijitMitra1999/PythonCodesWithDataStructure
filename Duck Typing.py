class Pycharm :
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor :
    def execute(self):
        print("Spell Check")
        print("Compiling")
        print("Running")

class Laptop :
    def code(self,Ide):
        Ide.execute()

Ide = MyEditor()
lap1 = Laptop()
lap1.code(Ide)