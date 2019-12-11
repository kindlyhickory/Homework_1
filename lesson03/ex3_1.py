def div(a,b):
    c = a/b
    return c

a = float(input('Введите первое число a: '))
b = float(input('Введите второе число b: '))
try:
    print(f'Деление числа a на число b: {div(a,b)}')
except ZeroDivisionError:
    print('На ноль делить нельзя')
except ValueError:
    print('Это не число')