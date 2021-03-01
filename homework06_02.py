# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.


class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def result(self):
        self.weight = 25
        self.thickness = 5
        result = self.length * self.width * self.weight * self.thickness / 1000
        print(f'Нужно {result} тонн асфальта')


road_to_village = Road(5000, 20)
road_to_village.result()
