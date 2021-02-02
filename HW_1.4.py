num = int(input('Введите целое положительное число: '))
max_n = num % 10
num = num // 10

while num > 0:
    if num % 10 > max_n:
        max_n = num % 10
    num = num // 10

print(f'Самая большая цифра: {max_n}')
