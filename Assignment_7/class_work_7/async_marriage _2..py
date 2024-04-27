import time
import random
import asyncio

#  in async any which of functions independently are run.


async def marriage(name):
    global counter
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print(f"{name} married after {r} years")
  


async def main():
    
        await asyncio.gather(marriage("mammad"), marriage("gholi"), marriage("goli"), marriage("alex"))

   


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in { total_time} seconds")