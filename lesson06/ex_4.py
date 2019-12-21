import random


class Car:
    def __init__(self):
        self.speed = random.randint(0, 90)
        self.color = input('Цвет машины: ')
        self.name = input('Название машины ')
        self.is_police = input('Машина полицейская True или False ')

    def show_speed(self):
        print(self.speed)

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула {direction}')


class TownCar(Car):
    def info(self):
        print(f'Городская машина :{self.name} {self.color}.\nЕё скорость{self.speed}')
    def show_speed(self):
        if self.speed > 60:
            print(f'Ваша скорость: {self.speed}. Превышение скорости')
        else:
            print(self.speed)


class SportCar(Car):
    def info(self):
        print(f'Спортивная машина: {self.name} {self.color}.\nЕё скорость{self.speed}')


class WorkCar(Car):
    def info(self):
        print(f'Рабочая машина: {self.name} {self.color}.\nЕё скорость {self.speed}')
    def show_speed(self):
        if self.speed > 40:
            print(f'Cкорость: {self.speed}. Превышение скорости')


class PoliceCar(Car):
    def info(self):
        print(f'Полицейская машина: {self.name} {self.color}.\n {self.speed}')

direction=['налево', 'направо']
worker_car = WorkCar()
worker_car.info()
worker_car.show_speed()
worker_car.go()
worker_car.stop()
worker_car.go()
worker_car.turn(direction[random.randint(0,1)])
