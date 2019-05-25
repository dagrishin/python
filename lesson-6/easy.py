# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:
    def __init__(self, speed=100, color='red', name='ford', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('остановилась')

    def turn(self, direction):
        print(f'повернула({direction})')


class SportCar:
    def __init__(self, speed=100, color='red', name='ford', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('остановилась')

    def turn(self, direction):
        print(f'повернула({direction})')


class WorkCar:
    def __init__(self, speed=100, color='red', name='ford', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('остановилась')

    def turn(self, direction):
        print(f'повернула({direction})')


class PoliceCar:
    def __init__(self, speed=100, color='red', name='ford', is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('остановилась')

    def turn(self, direction):
        print(f'повернула({direction})')

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, speed=100, color='red', name='ford', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('остановилась')

    def turn(self, direction):
        print(f'повернула({direction})')


class TownCar(Car):
    def __init__(self, speed=100, color='black', name='ford', is_police=False):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):
    def __init__(self, speed=300, color='red', name='ferrari', is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed=100, color='red', name='jeep', is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed=50, color='green', name='lada', is_police=True):
        super().__init__(speed, color, name, is_police)
