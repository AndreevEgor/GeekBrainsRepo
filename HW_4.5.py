from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]
new_list = reduce(lambda a, b: a + b, my_list)

print(new_list)

