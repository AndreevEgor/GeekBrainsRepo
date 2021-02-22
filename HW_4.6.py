from itertools import count, cycle

for i in count(int(input('Введите стартовое значение: '))):
    print(i)
    if i == 100:
        break

my_count = 0
my_list = [1, False, -10, 'HI', True]
for el in cycle(my_list):
    print(el)
    my_count += 1
    if my_count == 100:
        break


