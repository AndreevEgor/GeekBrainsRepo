time_sec = int(input('Введите количество секунд: '))
hours = time_sec // 3600
residue = time_sec % 3600
minutes = residue // 60
seconds = residue % 60

# Простой вариант, но выдает некорректный формат
# time = f'{hours}:{minutes}:{seconds}'

time = '%02d:%02d:%02d' % (hours, minutes, seconds)

print(time)
