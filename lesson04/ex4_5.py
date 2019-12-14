from functools import reduce

def multiplication(prev_el,el):
    return prev_el*el


even_numbered = [el for el in range(100, 1001) if el % 2 == 0]

print(f'Чётные числа: {even_numbered},\nИх произведение: {reduce(multiplication, even_numbered)}')