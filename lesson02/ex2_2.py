random_list = []
while True:
    try:
        length = int(input('Введите длину списка: '))

        for i in range(length):
            random_list.append(input('Введите элемент: '))

        if len(random_list) % 2 == 0:
            for i in range(0, len(random_list), 2):
                random_list[i], random_list[i + 1] = random_list[i + 1], random_list[i]
            print(random_list)
        else:
            for i in range(0, len(random_list)-1, 2):
                random_list[i], random_list[i + 1] = random_list[i + 1], random_list[i]
            print(random_list)
        break
    except ValueError:
        print('Это не число')
