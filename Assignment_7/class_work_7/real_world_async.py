import time
import random
import asyncio

async def get():
    print("Get started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print(f"Get ended in {r} second")


def extract():
    print("Extract started")
    r = random.randint(0,10)
    time.sleep(r)
    print(f"Extract ended in {r} second")


async def download():
    print("download started")
    await get()
    extract()

async def printer():

    print("printer started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print(f"printer ended in {r} second")

async def ai_video():
    print("AI video started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print(f"AI video ended in {r} second")
async def ai_audio():
    print("AI audio started")
    r = random.randint(0,10)
    await asyncio.sleep(r)
    print(f"AI audio ended in {r} second")
def ai_mix():
    print("Mix started")
    r = random.randint(0,10)
    time.sleep(r)
    print(f"Mix ended in {r} second")

async def ai():
    print("AI started")
    await asyncio.gather(ai_video() , ai_audio())
    ai_mix()
    print(f"AI ended")

async def main():
    await asyncio.gather(download(),printer(),ai())
    print("Main ended") 



if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Executed in { total_time} seconds")