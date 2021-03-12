
class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._widht = width


    def calculation(self):
        return f'{self._lenght}м * {self._widht}м * 25кг * 5см = {(self._lenght * self._widht * 25 * 5) / 1000}т'


my_road = Road(5000, 20)
print(my_road.calculation())



