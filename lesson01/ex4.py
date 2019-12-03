num = int(input('Введите целое положительное число: '))

max = num % 10

while num // 10 != 0:
    dig = num % 10
    num = num // 10
    if dig >= max:
        max = dig
if (num // 10) == 0:
    if num % 10 >= max:
        max = num % 10
print(f'Максимальная цифра из вашего числа: {max}')
