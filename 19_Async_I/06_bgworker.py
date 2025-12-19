import asyncio
import time
import threading

def background_worker():
    while True:
        time.sleep(1)
        print("logging the system health...")

async def fetch_orders():
    await asyncio.sleep(3)
    print("Order fetched succesfully...")

threading.Thread(target=background_worker, daemon=True).start()
asyncio.run(fetch_orders())


#daemon threads are background threads which automatically shut down when the main thraed shuts down