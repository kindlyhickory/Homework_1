from abc import ABC,abstractmethod

class Clothes(ABC):
    @abstractmethod
    def __init__(self, param):
        self.param = param
    def __add__(self,other):
        return f'Общий расход ткани: {round((round(self.param/ 6.5 + 0.5, 2)) + (round(other.param * 2 + 0.3, 2)),2)}'


class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)
        self.consumption = round(self.param / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Расход ткани для пальто {self.consumption}'


class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param)
        self.consumption = round(self.param * 2 + 0.3, 2)

    def __str__(self):
        return f'Расход ткани для костюма {self.consumption}'


coat = Coat(4)
suit = Suit(4)
print(coat)
print(suit)
print(coat+suit)
