#       Abstract class Import
from abc import ABC, abstractmethod

class Computer(ABC) :
    @abstractmethod
    def process(self):
        pass

class Laptop (Computer):
    def process(self):
        print("It's Running")

class Whiteboard(Computer):
    def write(self):
        print("It's Writing")
class Programmer :
    def work(self,com):
        print("Solving Bugs")
        com.process()
# com = Computer()
# com.process()

com1 = Laptop()
com1.process()
com2 = Whiteboard()
prog1 = Programmer()
prog1.work(com2)