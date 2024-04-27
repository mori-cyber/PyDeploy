import asyncio

async def fn1():
    print("one")
    await asyncio.sleep(1)
    # await fn2()
    # asyncio.create_task(fn2()) #for run one functiones
    # asyncio.gather(fn2(), fn3())# for run many functions
    await asyncio.gather(fn2(), fn3())

    await asyncio.sleep(1)
    print("four")
    await asyncio.sleep(1)
    print("five")


async def fn2():
    print("two")
    await asyncio.sleep(1)
    print("three")

async def fn3():
    print("six")
    await asyncio.sleep(1)
    print("seven")

asyncio.run(fn1())