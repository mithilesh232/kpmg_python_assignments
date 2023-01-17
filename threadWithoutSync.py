from threading import *
import time
def wish(name):
    for i in range(10):
        print("good evening:",end='')
        time.sleep(2)
        print(name)
t1=Thread(target=wish,args=("martin",))
t2=Thread(target=wish,args=("sandeep",))
t1.start()
t2.start()