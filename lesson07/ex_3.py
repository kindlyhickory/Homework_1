class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return f'Сложение клеток: {self.cells + other.cells}'

    def __sub__(self, other):
        if self.cells - other.cells >= 0 :
            return f'Вычитание клеток: {self.cells - other.cells}'
        elif other.cells - self.cells >=0 :
            return f'Вычитание клеток: {other.cells - self.cells}'
        else:
            return('Вычитание клеток невозможно')

    def __mul__(self, other):
        return f'Умножение клеток: {self.cells * other.cells}'

    def __truediv__(self,other):
        return f'Деление клеток: {round(self.cells / other.cells)}'

    def make_order(self,in_row):
        self.rows = self.cells//in_row
        remains = self.cells - in_row*self.rows
        rows_of_cells = ['*'*in_row for i in range(self.rows)]
        rows_of_cells.append('*'*remains)
        return '\n'.join(rows_of_cells)

cell_1 = Cell(50)
cell_2 = Cell(20)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(cell_1.make_order(11))