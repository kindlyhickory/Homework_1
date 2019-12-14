def fibo_gen(n):
    global i
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
        yield factorial


n = int(input('Введите факториал скольки вы хотите посчитать: '))
for factorial in fibo_gen(n):
    print(f'{i}! = {factorial}')
