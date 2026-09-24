# gather task

import asyncio
import time

async def fetch(delay, id):
    print(f'Starting on fetch id {id} taking {delay} seconds')
    # await the completion of sleep, event loop goes on with other stuffs
    # the finishing of sleep will awake event loop
    await asyncio.sleep(delay)  
    print(f'Fetch id {id} completed, taking {delay} seconds')
    return id

async def bad_func(delay, id):
    await asyncio.sleep(delay)
    raise ValueError(f'Task {id} produces an error.')

async def main():

    ## task
    # can also be created with task = asyncio.create_task(fetch(2, 1))
    task1 = asyncio.create_task(fetch(2, 1))
    task2 = asyncio.create_task(fetch(3, 2)) 
    task3 = asyncio.create_task(fetch(1, 3))

    # NOTE Exception handling, assume one of the functions is a bad function
    # coro2 will keep running because gather() abandon the remaining task
    task4 = asyncio.create_task(bad_func(2, 4))
    # task4 = asyncio.create_task(fetch(1, 4))

    ## NOTE gather: unpack a list of tasks wtih *
    try:
        results = await asyncio.gather(*[task1, task2, task3, task4])
    except ValueError as e:
        print(e)
    print(' the main is finished')

    # NOTE gather doesn't correctly cancel the rest of tasks upon exception
    # on the contrary, the remaining tasks keep running (unless the main finishes and break them)
    # Here is the proof: if we await task2, task2 is long enough to outlive the exception
    await task2
    print('in exception case, task 2 is not cancelled and will keep running')


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'Total time = {end - start:.3f}s')   # task 1, 2, 3 ran concurrently, total time = the longest = 3s