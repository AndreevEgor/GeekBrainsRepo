orig_list = [40, 59, 3, 83, 100, 1, 1, 46, 15, 100, 1000]
new_list = [el for i, el in enumerate(orig_list) if orig_list[i-1] < orig_list[i]]
print(new_list)
