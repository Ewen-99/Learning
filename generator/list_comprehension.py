my_nums = [x*x for x in [1, 2, 3, 4, 5]]
print(my_nums)  #NOTE the result is already out and stored in a list
for num in my_nums:
    print(num)

my_nums = (x*x for x in [1, 2, 3, 4, 5])
print(my_nums)
for num in my_nums:
    print(num)    #NOTE only run the next item when called next()
