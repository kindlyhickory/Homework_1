my_list = [88, 55, 34, 19, 12]
try:
    dig = float(input('Введите целое число: '))
    if dig in my_list:
        my_list.reverse()
        index = my_list.index(dig)
        my_list.insert(index, dig)
        my_list.reverse()
    else:
        for i in range(len(my_list)):
            if dig > my_list[i]:
                my_list.insert(i, dig)
                break
            elif dig < my_list[-1]:
                my_list.append(dig)
                break
    print(my_list)
except ValueError:
    print('Это не число')
