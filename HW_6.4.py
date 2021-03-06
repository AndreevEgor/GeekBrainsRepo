class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {"налево" if direction == 0 else "направо"}')

    def show_speed(self):
        print(f'{self.color} {self.name} движется со скоростью {self.speed} км')


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f'{self.name} движется со скоростью {self.speed} км')
        else:
            print(f'{self.name} нарушает скоростной режим, двигаясь со скоростью {self.speed} км')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f'{self.name} движется со скоростью {self.speed} км')
        else:
            print(f'{self.name} нарушает скоростной режим, двигаясь со скоростью {self.speed} км')


class PoliceCar(Car):
    pass


car = Car(70, 'Красная', 'Ferrari', 0)
car.go()
car.stop()
car.turn(1)
car.show_speed()
town_car = TownCar(80, 'Белая', 'Toyota', 0)
town_car.go()
town_car.stop()
town_car.turn(0)
town_car.show_speed()



