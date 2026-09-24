# Use processes
# the setup is expensive, only worth it if the cpu work is really heavy

# case1: baseline
# range(0, 1000000)
# step one: 13.98s
# step two: 10.33s

# case2: heavy cpu work
# range(0, 10000000)
# step one: 11.50s
# step two: 8.72s

# case3: heavy io work
# for i in range(0, 200):
# step one: 13.51s
# step two: 11.20s

import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import random
import time

def io_work(id):
    # print(f'Start io_work no. {id}')
    time.sleep(random.random())
    data = random.random()
    # print(f'Finish io_work no. {id}')
    return data

def cpu_work(data):
    for i in range(0, 1000000):
        data += i
    return data


async def main():

    t0 = time.perf_counter()
    loop = asyncio.get_running_loop()

    ## Step1: Get all IO
    futures = []
    with ProcessPoolExecutor() as pool:
        for i in range(0, 200):
            future = loop.run_in_executor(pool, io_work, i)
            futures.append(future)
    data = await asyncio.gather(*futures)
    print('All IO task completed')
    # print(data)
    t1 = time.perf_counter()

    ## Step2: execute cpu_work
    with ProcessPoolExecutor() as pool:
        for d in data:
            future = loop.run_in_executor(pool, cpu_work, d)
            futures.append(future)
    result = await asyncio.gather(*futures)
    print('All CPU task completed')
    print(result)
    t2 = time.perf_counter()

    print(f'step one: {t1 - t0:.2f}s')
    print(f'step two: {t2 - t1:.2f}s')

if __name__ == "__main__":
    asyncio.run(main())
