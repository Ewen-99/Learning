import random
print(random.random())


try:
    a = 1 + 'a'
except TypeError as e:
    print(f'error, {e}')

print('end')

raise TypeError('this is another error')

print('end2')