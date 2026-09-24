# use process pool to run synchronous functions

import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def fetch(delay, id):
    print(f'Starting on fetch id {id} taking {delay} seconds')
    # await the completion of sleep, event loop goes on with other stuffs
    # the finishing of sleep will awake event loop
    time.sleep(delay)  
    print(f'Fetch id {id} completed, taking {delay} seconds')
    return id

def blocking_task(delay, id):   # blocking code is no longer asyn def -> calling doesn't run coroutine function!
    print(f'Working on a synchronous function id {id} which will take {delay} seconds')
    time.sleep(delay)   # non awaitable, error if putting an await in front
    print(f'Completed the synchronous function id {id} which took {delay} seconds')
    return id

async def main():

    # call to get the loop
    loop = asyncio.get_running_loop()

    # start multiple processes
    with ProcessPoolExecutor() as pool:
        task1 = loop.run_in_executor(pool, blocking_task, 5, 1)
        task2 = loop.run_in_executor(pool, fetch, 3, 2)
        task3 = loop.run_in_executor(pool, fetch, 1, 3)

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'Total time = {end - start:.3f}s')   # taking longer than 5s because of setup time