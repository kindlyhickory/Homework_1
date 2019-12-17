with open('ex_5.txt','w') as file:
    amount = 0
    file.write(input('Введите через пробел числа, которые вы хотите просуммировать: '))

with open('ex_5.txt','r') as file:
    a = file.read().split()
    try:
        for i in range(len(a)):
            amount += int(a[i])
        print(amount)
    except ValueError:
        print('Вы ввели не число')