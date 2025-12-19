from multiprocessing import Process
from time import time

def crunch_number():
    print("Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print("Count process ended...")

if __name__ == "__main__":
    start = time()

    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time()
    print(f"total time taken in multi-processing : {end-start :.2f} seconds")



"""
1. How the GIL blocks threads:
   - GIL (Global Interpreter Lock) ensures that only one thread can execute Python bytecode at any moment.
   - Even if multiple threads are created, the GIL forces them to run one at a time.
   - This means CPU-bound programs do NOT run in parallel when using threads.
   - The GIL does NOT affect multiprocessing because each process has its own Python interpreter and its own GIL.
   - As a result, threads seem to "take turns" instead of running simultaneously for CPU-heavy tasks.

2. How a mutex works:
   - A mutex (Lock) enforces mutual exclusion so only one thread can access a shared resource at any time.
   - When a thread calls lock.acquire(), other threads attempting to acquire the same lock must wait.
   - After the thread finishes its critical work, it releases the lock using lock.release().
   - Mutex prevents race conditions where multiple threads modify the same shared variable at the same time.
   - In the current program, no mutex is needed because each thread/process uses its own local variables, so nothing is shared.

"""
