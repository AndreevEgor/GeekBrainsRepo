class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}.Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Ручка {self.title}. Запуск отрисовки')


class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш {self.title}. Запуск отрисовки')


class Handle(Stationery):
    def draw(self):
        print(f'Маркер {self.title}. Запуск отрисовки')


stationery = Stationery('Что-то пишущее')
stationery.draw()
pen = Pen('Staff')
pen.draw()
pencil = Pencil('Brauberg')
pencil.draw()
handle = Handle('Attache')
handle.draw()
