# Using coroutine only creates no concurrency

import asyncio
import time

async def fetch(id, delay):
    print(f'Starting on fetch id {id} taking {delay} seconds')
    # await the completion of sleep, event loop goes on with other stuffs
    # the finishing of sleep will awake event loop
    await asyncio.sleep(delay)  
    print(f'Fetch id {id} completed, taking {delay} seconds')
    return id

async def main():

    ## coroutine
    # coroutine is ready but 'lazy', they are not scheduled into the loop yet
    coro1 = fetch(1, 2)
    coro2 = fetch(2, 3)
    coro3 = fetch(3, 1)

    # coroutines are scheduled into the loop one by one (not at once like tasks),
    # creating no benefit of concurrency at all
    result1 = await coro1   
    result2 = await coro2   # this line only execute when coro1 is done and wake up main()
    result3 = await coro3   

    print(result1, result2, result3)

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'Total time = {end - start:.3f}s')   # No concurrency: 6s