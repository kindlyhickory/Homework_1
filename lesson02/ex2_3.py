while True:
    try:
        month = int(input('Введите номер месяца: '))
        months_dict = {1: 'зима январь',
                       2: 'зима февраль',
                       3: 'весна март',
                       4: 'весна апрель',
                       5: 'весна май',
                       6: 'лето июнь',
                       7: 'лето июль',
                       8: 'лето август',
                       9: 'осень сентябрь',
                       10: 'осень октябрь',
                       11: 'осень ноябрь',
                       12: 'зима декабрь'
                       }
        months_list = ['зима январь', 'зима февраль', 'весна март', 'весна апрель', 'весна май', 'лето июнь',
                       'лето июль',
                       'осень сентябрь',
                       'лето август', 'осень октябрь', 'осень ноябрь', 'зима декабрь']
        print(f'Время года cо словаря: {months_dict[month]}')
        print(f'Время года со списка: {months_list[month - 1]}')
        break
    except IndexError:
        print('Такого времени года не существует')
    except ValueError:
        print('Это не число')
    except KeyError:
        print('Такого времени года не существует')
