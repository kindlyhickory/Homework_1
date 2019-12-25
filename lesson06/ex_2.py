class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        self.weights = self._length * self._width * 25 * 5 / 1000
        print(f'{self.weights} тонн')

road_1 = Road(20, 5000)
road_1.weight()
