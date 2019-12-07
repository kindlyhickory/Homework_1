random_str = input('Введите строку разделенную пробелами: ')
if ',' not in random_str:
    splitted = random_str.split()
    for i in range(len(splitted)):
        if len(splitted[i]) <= 10:
            print(f'Номер строки:{i + 1} {splitted[i]}')
        else:
            print(f'Номер строки:{i + 1} {splitted[i][0:10]}')
else:
    print('Ваша строка разделена не пробелами')
