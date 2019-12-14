from random import randint

my_list = [randint(-30,30) for i in range(20)]
print(f'Случайный список: {my_list}')
new_list = [my_list[i+1] for i in range(len(my_list) - 1) if my_list[i] < my_list[i+ 1]]
print(f'С элементами {new_list}')
