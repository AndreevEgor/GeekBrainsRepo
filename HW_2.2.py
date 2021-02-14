my_list = []

while True:
    i = input('Вводите элементы списка (для завершения введите "Stop"): ')
    if i.capitalize() == 'Stop':
        break
    my_list.append(i)

print(my_list)

if len(my_list) % 2 != 0:
    my_list[:-1:2], my_list[1:-1:2] = my_list[1:-1:2], my_list[:-1:2]
else:
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
print(my_list)
