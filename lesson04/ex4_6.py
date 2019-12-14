from itertools import cycle, count


def stop(start, end):
    for el in count(start):
        if el > end:
            break
        else:
            print(el)
    return


def cycle_1(my_list, end):
    i = 0
    for element in cycle(my_list):
        if i > end:
            break
        print(element)
        i += 1


my_list = "Geekbrains"

start = int(input('Введите с какого числа начнется итератор: '))
end = int(input('Введите на каком числе закончится итератор: '))
stop(start=start, end=end)

end_1 = int(input('Сколько раз нужно повторить элемент из списка: '))
cycle_1(my_list=my_list, end=end_1)
