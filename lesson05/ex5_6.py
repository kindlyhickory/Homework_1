with open('ex_6.txt', 'r', encoding='utf-8') as file:
    my_dict = {}
    for line in file:
        time = 0

        index = line.find('(пр)')
        if index == -1:
            pass
        else:
            dig = line[index - 3: index]
            time = time + int(dig)

        index = line.find('(лаб)')
        if index == -1:
            pass
        else:
            dig = line[index - 3: index]
            time = time + int(dig)

        index = line.find('(л)')
        if index == -1:
            pass
        else:
            dig = line[index - 3: index]
            time = time + int(dig)
        splitted_line = line.split()
        my_dict[splitted_line[0]] = time
    print(my_dict)
