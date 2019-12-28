class ZeroDiv(Exception):
    def __init__(self,text):
        self.text = text

input_dig_1 = int(input('Введите число, которое хотите поделить: '))
input_dig_2 = int(input('Введите число, на которое хотите поделить: '))

try:
    if input_dig_2 == 0:
        raise ZeroDiv('Вы ввели ноль. На ноль делить нельзя')
    output_dig = input_dig_1/input_dig_2
except ZeroDiv as err:
    print(err)
except TypeError:
    print('Вы ввели не число')
else:
    print(output_dig)


