my_str = str(input('Введите несколько слов через пробел: '))
my_list = my_str.split(' ')
count = 1

while count <= len(my_list):
    for i in my_list:
        print(f'{count}: {i[:10]}')
        count += 1
