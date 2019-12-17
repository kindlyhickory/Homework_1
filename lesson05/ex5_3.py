person = []
average = 0
with open('ex_3.txt', 'r') as file:
    for i, line in enumerate(file):
        name = line.split()[0]
        salary = int(line.split()[1])
        if salary < 20000:
            person.append(name)
        average += salary
    average = average / i + 1
    print(f'Средняя зарплата: {average},\nЗарплата < 20000: {person}')
