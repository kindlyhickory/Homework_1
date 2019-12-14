from sys import argv

def earnings(time,rate,prize):
    earn = float(time)*float(rate) + float(prize)
    return earn
try:
    print(f'Ваша зарплата: {earnings(time = argv[1], rate=argv[2], prize = argv[3])}')
except ValueError:
    print('Вы ввели не числа')