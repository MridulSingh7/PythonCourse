import threading
import time

#using only single thread in this example

def boil_milk():
    print(f"Boiling milk...")
    time.sleep(3)
    print(f"Milk finished boiling...")


def toast_bun():
    print(f"Toasting the bun...")
    time.sleep(3)
    print(f"Done witht he bun toast...")

start = time.time()
t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(f"time taken using single thread : {end-start:.2f}")