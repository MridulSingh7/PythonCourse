import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):
        count+=1
    print(f"{threading.current_thread().name} finished brewing....")


thread1 = threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"total time taken : {end-start :.2f} seconds")



'''
why gil?
memory management is not efficient in multiprocessing.
gil ensures no two different threads can change the memory at the same time

race conditions?
when two or more threads are trying to access same memory  
 
 
How start and end time works:
  - start = time.time() saves the timestamp just before starting threads.
  - end = time.time() saves timestamp after both threads have completed.
  - end - start gives the total execution duration in seconds.
'''