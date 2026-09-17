# Here we try keeping the sequence of creating tasks,
# but schuffling the sequence of awaiting them

# turns out tasks are executed according to the order of their creation, i.e. place on the schedule list, not the awwait
# but it is important to note that, you do need to await the finishing of the first awaited object, until the main() moves on

import asyncio
import time

async def fetch(delay, id):
    print(f'Starting on fetch id {id} taking {delay} seconds')
    # await the completion of sleep, event loop goes on with other stuffs
    # the finishing of sleep will awake event loop
    await asyncio.sleep(delay)  
    print(f'Fetch id {id} completed, taking {delay} seconds')

async def main():

    ## coroutine
    # coroutine is ready but 'lazy', they are not scheduled into the loop yet
    coro1 = fetch(2, 1)
    coro2 = fetch(3, 2)
    coro3 = fetch(1, 3)

    ## task
    # schedule list: task 1 -> 2 -> 3
    task1 = asyncio.create_task(coro1)
    task2 = asyncio.create_task(coro2)
    task3 = asyncio.create_task(coro3)

    ## await tasks
    # await order: task 3 -> 1 -> 2; execution 1 -> 2 -> 3
    result3 = await task3   # but main() will NOT move forward until task3 comes back
    result1 = await task1
    result2 = await task2

    print(result1, result2, result3)

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'Total time = {end - start:.3f}s')   # concurrent, the execution order is still 1 - 2 - 3