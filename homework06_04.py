# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} - {self.speed} км/ч')

        if self.speed > 60:
            return f'Скорость автомобиля {self.name} превышена!'
        else:
            return f'Автомобиль {self.name} движется с нормальной скоростью.'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} - {self.speed} км/ч')

        if self.speed > 40:
            return f'Скорость автомобиля {self.name} превышена!'
        else:
            return f'Автомобиль {self.name} движется с нормальной скоростью.'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - это полицейская машина.'
        else:
            return f'{self.name} - это гражданский автомобиль'


audi = SportCar(140, 'серая', 'Audi', False)
oka = TownCar(30, 'белая', 'Ока', False)
lada = WorkCar(70, 'желтая', 'Лада', False)
ford = PoliceCar(110, 'черный',  'Ford', True)

print(lada.turn_left())
print(f'{lada.show_speed()}')
print(f'{lada.name} полицейская машина? {lada.is_police}')

print(f'Когда {oka.turn_right()}, {audi.turn_left()}')
print(f'{audi.name} полицейская машина? {audi.is_police}')
print(f'{audi.show_speed()}')
print(f'{oka.show_speed()}')

print(ford.police())
print(ford.show_speed())
