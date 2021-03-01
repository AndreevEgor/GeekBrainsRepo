def my_f(num1, num2, num3):
    try:
        return sum((num1, num2, num3)) - min(num1, num2, num3)
    except TypeError:
        return 'Вводите только цифры'


print(my_f(20, 100, 2))
