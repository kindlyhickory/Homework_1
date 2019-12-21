my_list = [1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 9, 0, 0, 10]

print([el for el in my_list if my_list.count(el) <= 1])
