# task group

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

    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(fetch(2, 1))   # NOTE syntax: tg.create_task; create_task is a method under class instance task group
            task2 = tg.create_task(fetch(3, 2)) 
            task3 = tg.create_task(fetch(1, 3))

        # NOTE Exception handling, assume one of the functions is a bad function
        # coro2 will keep running because gather() abandon the remaining task
            task4 = tg.create_task(bad_func(2, 4))
            # task4 = tg.create_task(fetch(1, 4))

        print('All tasks run normally')

    except* ValueError as e:
        print(e)
        print(f'you have finished: task {task1.result()} {task3.result()}')
        print('one of the task failed. so you do not see task 2 finished (it is canceled)')

    # NOTE gather doesn't correctly cancel the rest of tasks upon exception
    # But taskgroup will cancel the remaining task
    # Here is the proof: if we await task2, there will be an error, because task2 has been cancelled and is not awaitable
    try:
        await task2
        print('in exception case, task 2 is not cancelled and will keep running')
    except asyncio.exceptions.CancelledError as e:
        print('task 2 has been cancelled. so no further result2 can be awaited.')
        print(e)

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'Total time = {end - start:.3f}s')   # task 1, 2, 3 ran concurrently, total time = the longest = 3s