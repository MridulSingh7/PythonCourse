#we use async def
#we declare a coroutine -> special function that can be paused anytime
import asyncio

async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(2) #similar to time.sleep
    print("Chai is ready")

asyncio.run(brew_chai()) #.run executes the coroutine 


async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(2)
    print(f"{name} is ready...")

#we can have our main function a async function too and we can have multiple coroutines in it and can await them inside it


async def main():
    #gather will collect all coroutines one by one in order and store them
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Green Chai"),
        brew("Ginger Chai"),
    )
#when the main function is ran in asyncio, the gathered coroutines will run one by one as listed inside the gather 
asyncio.run(main())


'''
await waits in a non blocking fashion, it means it wont block other operations while awaiting
try the same program with time.sleep(2) instead of asyncio.sleep(2),
in time.sleep your code will stop untill 2 seconds but asyncio.sleep will just await the next execution for 2 seconds, the program doesnt stop.

'''