import threading
chai_stock = 0

def restock():
    global chai_stock
    for _ in range(10000):
        chai_stock+=1

threads = [ threading.Thread(target=restock) for _ in range(2)]

for t in threads : t.start()
for t in threads : t.join()

print("Chai stock : ", chai_stock)



'''
race condition?
when multiple threads are modifying same data and no one can decide who will modify it first 
use deadlock in these conditions
'''