def my_func(a, b, c):
    min_val = min(a, b, c)
    if a == min_val:
        return b + c
    elif b == min_val:
        return a + b
    else:
        return a + b


a = float(input('Введите первое число a: '))
b = float(input('Введите первое число b: '))
c = float(input('Введите первое число c: '))
print(f'Сумма максимальных двух чисел: {my_func(a, b, c)}')
