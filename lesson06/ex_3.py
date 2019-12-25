class Worker:
    def __init__(self):
        self.name = input('Name: ')
        self.surname = input('Surname: ')
        self._income = {'wage': input('Ваш оклад: '), 'bonus': input('Ваша премия: ')}


class Position(Worker):
    def get_full_name(self):
        print(f'Full name: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Total income: {int(self._income["wage"]) + int(self._income["bonus"])}')


worker_1 = Position()
worker_1.get_full_name()
try:
    worker_1.get_total_income()
except ValueError:
    print('ValueError')
