# forgetting awaiting a task can lead to finishing the main() without task2

import asyncio
import time

async def fetch(delay, id):
    print(f'Starting on fetch id {id} taking {delay} seconds')
    # await the completion of sleep, event loop goes on with other stuffs
    # the finishing of sleep will awake event loop
    await asyncio.sleep(delay)  
    print(f'Fetch id {id} completed, taking {delay} seconds')
    return id

async def main():

    ## coroutine
    # coroutine is ready but 'lazy', they are not scheduled into the loop yet
    coro1 = fetch(2, 1)
    coro2 = fetch(3, 2)
    coro3 = fetch(1, 3)

    ## task
    # can also be created with task = asyncio.create_task(fetch(2, 1))
    task1 = asyncio.create_task(coro1)
    task2 = asyncio.create_task(coro2)
    task3 = asyncio.create_task(coro3)

    ## await tasks
    result1 = await task1
    result2 = task2    # forget to await task2, the loop skip this line as task 2 has not been finished
    result3 = await task3  

    print(result1, result2, result3)

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'Total time = {end - start:.3f}s')   # task 1, 2, 3 ran concurrently, total time = the longest = 3s