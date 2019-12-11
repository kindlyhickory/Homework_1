def my_func_1(x,y):
    return x**y

def my_func_2(x,y):
    s=1/x
    for i in range(abs(y)-1):
        s=s*(1/x)
    return s
a=float(input('Введите число: '))
b=int(input('Введите целое отрицательное число: '))
print(my_func_1(a,b))
print(f'{my_func_2(a,b):.5f}')
