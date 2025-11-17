# def square(num):
#     return num**2

# other_square = lambda num: num ** 2

# print(square(9))
# test = square
# print(test(9))
# print(other_square(9))

import random
my_list = []
for i in range(10):
    #randrange is not inclusive on the far end.
    #randint is inclusive
    my_list.append(random.randrange(5,50))


# The following two codes return the same thing.
def filter(in_func, list):
    new_list = []
    for item in list:
        if in_func(list[item]):
            new_list.append(item)
    return new_list

filter = lambda func, list: [item for item in list if func[i]]