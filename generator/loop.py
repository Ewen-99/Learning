
print([x*x for x in [1, 2, 3, 4, 5]])

def square(num):
    result = []
    for x in num:
        result.append(x*x)
    return result

my_nums = square([1, 2, 3, 4, 5])
print(my_nums)

