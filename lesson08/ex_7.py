class Complexnumber:
    def __init__(self, i, j):
        self.Re = i
        self.Im = j

    def __add__(self, other):
        return f'{(self.Re+other.Re)}+({self.Im+other.Im})j'

    def __mul__(self, other):
        return f'{self.Re*other.Re - self.Im*other.Im}+{self.Re*other.Im + self.Im*other.Re}j'


i_1 = int(input('Введите вещественную часть первого числа: '))
j_1 = int(input('Введите мнимую часть первого числа'))
i_2 = int(input('Введите вещественную часть второго числа: '))
j_2 = int(input('Введите мнимую часть второго числа числа'))
dig_1 = Complexnumber(i_1, j_1)
dig_2 = Complexnumber(i_2, j_2)

print(dig_1+dig_2)
print(dig_1*dig_2)
