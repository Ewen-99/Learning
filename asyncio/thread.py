# use thread to run synchronous functions

import asyncio
import time

async def fetch(delay, id):
    print(f'Starting on fetch id {id} taking {delay} seconds')
    # await the completion of sleep, event loop goes on with other stuffs
    # the finishing of sleep will awake event loop
    await asyncio.sleep(delay)  
    print(f'Fetch id {id} completed, taking {delay} seconds')
    return id

def blocking_task(delay, id):   # NOTE blocking code is no longer asyn def -> calling doesn't run coroutine function!
    print(f'Working on a synchronous function id {id} which will take {delay} seconds')
    time.sleep(delay)   # non awaitable, error if putting an await in front
    print(f'Completed the synchronous function id {id} which took {delay} seconds')
    return id

async def main():

    ## blocking call
    task1 = asyncio.create_task(asyncio.to_thread(blocking_task, delay=5, id=1))    # use asyncio.to_thread() to run blocking code
    # NOTE input the parameters separately, so the function is not run immediately when called

    ## task
    task2 = asyncio.create_task(fetch(3, 2))
    task3 = asyncio.create_task(fetch(1, 3))

    ## await tasks
    result1 = await task1   # synchronous function, blocking the await
    result2 = await task2   # not executed until the completion of the blocking code
    result3 = await task3  

    print(result1, result2, result3)

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'Total time = {end - start:.3f}s')   # 5s concurrent, time = max(time) = blocking code 5s