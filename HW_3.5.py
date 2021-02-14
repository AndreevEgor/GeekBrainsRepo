def my_sum():
    s = 0
    while True:
        num_list = input('Введите числа через пробел, для завершения введите "S": ').upper().split()
        for i in num_list:
            if i == 'S':
                return s
            s += int(i)
        print(s)


print(my_sum())
