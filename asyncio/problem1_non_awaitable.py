# function like request is non awaitable

import asyncio
import time

async def fetch(delay, id):
    print(f'Starting on fetch id {id} taking {delay} seconds')
    # await the completion of sleep, event loop goes on with other stuffs
    # the finishing of sleep will awake event loop
    await asyncio.sleep(delay)  
    print(f'Fetch id {id} completed, taking {delay} seconds')
    return id

async def blocking_task(delay):
    print(f'Working on a synchronous function which will take {delay} seconds')
    time.sleep(delay)   # non awaitable, error if putting an await in front
    print(f'Completed the synchronous function which took {delay} seconds')

async def main():

    ## blocking call
    # a blocking call inside the task will not yield control to event loop
    # comment out the previous task 3 and uncomment here to try it out
    task1 = asyncio.create_task(blocking_task(5))

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
    print(f'Total time = {end - start:.3f}s')   # blocking code takes 5s, then two concurrent take 3 -> 8s in total