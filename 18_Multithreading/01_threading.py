import threading
import time


def take_orders():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(3)

def brew_chai():
    for i in range(1,4):
        print(f"Brewing Chai for #{i}")
        time.sleep(5)

#when you want to segregate two functions to two threads/simultaneous working of functions
#1.creating the thread
order_thread =  threading.Thread(target=take_orders)
brew_thread =  threading.Thread(target=brew_chai)

#to invoke(start) them 
order_thread.start()
brew_thread.start()
#example of multi threading, these two are working on different threads    

#when we need to wait for both to finish
order_thread.join()
brew_thread.join()

print("All orders taken and chai served")


'''
this is multi threading not multiprocessing
multi threading involves only one core, different threads of a single core are engaged
multiprocessing involes different cores  
this code was concurrency
'''