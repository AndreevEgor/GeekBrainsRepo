num_m = int(input('Введите номер месяца: '))

# Решение через   list
# seasons = ['winter', 'spring', 'summer', 'autumn']
# if num_m == 12 or num_m == 1 or num_m == 2:
#     print(seasons[0])
# elif num_m == 3 or num_m == 4 or num_m == 5:
#     print(seasons[1])
# elif num_m == 6 or num_m == 7 or num_m == 8:
#     print(seasons[2])
# elif num_m == 9 or num_m == 10 or num_m == 11:
#     print(seasons[3])
# else:
#     print('Введено некорректное значение')

# Решение через dict
seasons = {1: 'winter',
           2: 'winter',
           3: 'spring',
           4: 'spring',
           5: 'spring',
           6: 'summer',
           7: 'summer',
           8: 'summer',
           9: 'autumn',
           10: 'autumn',
           11: 'autumn',
           12: 'winter'}
print(seasons.get(num_m))
