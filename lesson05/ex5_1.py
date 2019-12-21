a = 1
with open('ex_1.txt', 'w') as file:
    while a:
        a=input('Введите данные: ')
        file.writelines([a,'\n'])