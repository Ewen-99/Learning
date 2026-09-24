def square_yield(num):
    for x in num:
        result = x * x
        print(f'the function execute the {x} time')
        print('before yield')
        yield result
        print('after yield')    # NOTE the loop only executes until the yield line

my_nums = square_yield([1, 2, 3, 4, 5])
print(my_nums)  #NOTE the function is not called yet. it is a generator object

print(next(my_nums))    #NOTE only run the next item when called next()
print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))


# NOTE loop over the generator object to get full result
def square(num):
    for x in num:
        result = x * x
        yield result

my_nums = square([1, 2, 3, 4, 5])
print(my_nums)
print('loop over the generator object to get full result')
for num in my_nums:    #NOTE only run the next item when called next() in the loop
    print(num)

