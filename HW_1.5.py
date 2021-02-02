proceeds = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержек: '))
if proceeds > costs:
    print('Фирма работает в плюс')
    profit = proceeds - costs
    staff = int(input('Введите количество сотрудников: '))
    profit_on_staff = f'На каждого из {staff} сотрудников приходится {profit/staff} прибыли'
    print(profit_on_staff)
elif proceeds == costs:
    print('Фирма работает в ноль')
else:
    print('Фирма работает в минус')
