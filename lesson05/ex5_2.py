with open('ex_2.txt','r') as file:
    for i,line in enumerate(file):
        print(f'Количество слов в {i+1} строке: {len(line.split())}')
    print(f'Строк всего в файле: {i+1}')
