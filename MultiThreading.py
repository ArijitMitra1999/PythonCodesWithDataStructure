import time
from threading import *

class Hello(Thread) :
    def run(self):
        for i in range(5) :
            print("Thread 1")
            time.sleep(1)
class Hii(Thread) :
    def run(self):
        for i in range(5):
            print("Thread 2")
            time.sleep(1)
t1 = Hello()
t2 = Hii()

#Thread Starting
t1.start()
time.sleep(0.2)
t2.start()

#If I Print Something In Main Thread at last then use join method to complete the process then print somethimg for main thread
t1.join()
t2.join()
print("Bye")