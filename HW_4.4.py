old_list = [35, 4, 4, 56, 56, 56, 100, 23, 1, 1, 1, 9]
new_list = [el for el in old_list if old_list.count(el) == 1]
print(new_list)
