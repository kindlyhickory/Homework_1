class OnlyDig(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
power = 'on'
while power == 'on':
    marker = 0
    try:
        input_data = input('Введите числа разделенные пробелом и stop, если хотите завершить: ')
        splitted_digs = input_data.split()
        joined_digs = ''.join(splitted_digs)
        if joined_digs.isdigit():
            my_list.extend(splitted_digs)
        else:
            for i in range(len(splitted_digs)):
                if splitted_digs[i].isdigit():
                    my_list.append(splitted_digs[i])
                elif splitted_digs[i] == 'stop':
                    power = 'off'
                else:
                    marker+=1
            if marker > 0:
                raise OnlyDig('Вы ввели не число')
    except OnlyDig as err:
        print(err)
    print(f'Ваш список: {my_list}')
