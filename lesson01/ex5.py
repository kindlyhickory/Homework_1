gain = float(input('Введите значение вашей выручки: '))
costs = float(input('Введите значение ваших издержек: '))

if gain > costs:
    print('Ваша выручка больше издержек')
    print(f'Ваша прибыль: {gain-costs}')
    profitability = (gain - costs)/gain * 100
    print(f'Ваша рентабельность составляет: {profitability:.1f}%')
    count = int(input('Какова численность работников: '))
    print(f'Размер прибыли на одного сотрудника: {((gain-costs)/count):.2f} рублей')
elif gain < costs:
    print('Ваша выручка меньше издержек')
else:
    print('Размер издрежек равен размеру выручки')

