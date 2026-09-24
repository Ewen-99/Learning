## Basic use
1. coroutine
2. task
3. sequence of running tasks -> loop

## Problem and derivatives:
# 1. blocking code
4. Problem 1 - non awaitable object, e.g. sychronous function like time.sleep(), blocking the loop
5. solution 1: thread - solve blocking code problem with threading
6. solution 2: process pool - solve blocking code problem with process pool

# 2. Multiple tasks
7. Problem 2 - forget to await -> break running tasks
8. solution1: gather -> by default, abandon the remaining tasks upon any failure
9. solution2: taskgroup -> correctly cancel all task upon any failure

## I/O bound or CPU bound
## thread vs. process 
10. 