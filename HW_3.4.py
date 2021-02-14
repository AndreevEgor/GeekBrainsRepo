def my_f(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Число X должно быть вещественным, число Y должно быть целым')
        return
    if x <= 0 or y >= 0:
        print('Число X должно быть положительным, число Y должно быть отрицательным')
        return
    return x ** y


print(my_f(2, -11))
