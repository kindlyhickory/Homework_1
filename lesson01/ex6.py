distance = float(input('Сколько километров вы пробежали за первый день: '))
point = float(input('Ваша цель: '))
day = 2
while distance < point:
    distance = distance + distance*0.1
    print(f'{day}-й день: {distance:.2f} километров')
    day = day + 1
print(f'Вы достигнете результата в {day-1} день')
