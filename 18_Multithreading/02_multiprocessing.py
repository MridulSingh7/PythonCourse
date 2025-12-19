from multiprocessing import Process
import time


def brew_chai(name):
    print(f"chai {name} is brewing...")
    time.sleep(3)
    print(f"chai {name} brewed.")


if __name__ == "__main__":
    #chai maker is creating and storing different processing objects
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai maker #{i+1}",))  # NOTE THE COMMA
        for i in range(3)
    ]

    # starting all processes, processes were stored in chai_makers list using list comprehension
    for p in chai_makers:
        p.start()

    # wait for all to complete
    for p in chai_makers:
        p.join()

    print("All chai served....")








'''
multiple cores are used in this:

we need to start all processes at once
and we need to wait for all to complete



Multiprocessing allows Python to run multiple tasks at the same time by using
multiple CPU cores. Each Process() creates a separate Python process with its
own memory space.

In this example, we create 3 processes where each worker brews chai. When we
call p.start(), all processes begin running simultaneously on different CPU
cores. This means the brewing work is done in parallel instead of waiting for
one to finish before starting the next.

p.join() is used to make the main program wait until that process is finished.
We call join() on all processes so the script waits for all chai makers to
complete their brewing. Once all processes are done, the final message
“All chai served...” is printed.
'''