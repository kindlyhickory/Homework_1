import json

with open('ex_7.txt', 'r', encoding='utf-8') as file:
    info = [{}, {}]
    average = 0
    profit = 0
    i = 0
    for line in file:
        splitted_line = line.split()
        profit = int(splitted_line[2]) - int(splitted_line[3])
        info[0][splitted_line[0]] = profit
        if profit < 0:
            pass
        else:
            i += 1
            average += profit
    info[1]['average profit'] = round(average / i, 2)
with open('ex_7_json.json', 'w') as file_2:
    json.dump(info, file_2)
