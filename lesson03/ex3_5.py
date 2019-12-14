def sum_1(dig_list):
    global s, el
    for i, el in enumerate(dig_list):
        if el == 'q' or el == 'Q':
            el = el.lower()
            print(f'Сумма ваших чисел: {s}\nПрограмма закончила работу по символу q')
            return
        else:
            s = s + int(dig_list[i])
    return print(f'Сумма ваших чисел: {s}')


s = 0
el = 0
while el != 'q':
    try:
        string = input(
             'Введите строку чисел разделенных пробелом. Если хотите выйти из программы, то напишите "q" или "Q" ')
        nums = string.split()
        sum_1(nums)
    except ValueError:
        print('Это не число и не специальный символ "Q"')
