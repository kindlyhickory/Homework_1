with open('ex_4.txt','r') as file:
    with open('ex_4_2.txt','w') as file_2:
        for line in file:
            splitted_line = line.split('-')
            if splitted_line[0] == 'One ':
                splitted_line[0]='Один -'
                file_2.writelines(splitted_line)
            elif splitted_line[0] == 'Two ':
                splitted_line[0] = 'Два -'
                file_2.writelines(splitted_line)
            elif splitted_line[0] == 'Three ':
                splitted_line[0] = 'Три -'
                file_2.writelines(splitted_line)
            elif splitted_line[0] == 'Four ':
                splitted_line[0] = 'Четыре -'
                file_2.writelines(splitted_line)