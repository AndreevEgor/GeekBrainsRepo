from time import sleep


class TrafficLight:
    __color = ['КРАСНЫЙ', 'ЖЕЛТЫЙ', 'ЗЕЛЕНЫЙ']

    def running(self):
        tl = TrafficLight
        while True:
            print(f'Горит \x1b[6;30;41m {tl.__color[0]} \x1b[0m сигнал светофора')
            for i in range(7, 0, -1):
                sleep(1)
                print(i)
            print(f'Горит \x1b[6;30;43m {tl.__color[1]} \x1b[0m сигнал светофора')
            for i in range(2, 0, -1):
                sleep(1)
                print(i)
            print(f'Горит \x1b[6;30;42m {tl.__color[2]} \x1b[0m сигнал светофора')
            for i in range(5, 0, -1):
                sleep(1)
                print(i)


TL = TrafficLight()
TL.running()
