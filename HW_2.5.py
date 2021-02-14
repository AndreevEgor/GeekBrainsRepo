import bisect
num = int(input('Введите натуральное число: '))
list1 = [7, 5, 5, 5, 3, 2, 2]
list1.sort()
bisect.insort_right(list1, num)
list1.reverse()
print(list1)
