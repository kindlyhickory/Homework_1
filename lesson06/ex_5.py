class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('Отрисовка ручкой')


class Pencil(Stationary):
    def draw(self):
        print('Отрисовка карандашом')


class Handle(Stationary):
    def draw(self):
        print('Отрисовка маркером')


handle = Handle('маркер')
handle.draw()
pencil = Pencil('карандаш')
pencil.draw()
pen = Pen('ручка')
pen.draw()
