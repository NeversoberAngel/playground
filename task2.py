"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

s_length = float(input('Type in the length of the road section(m): '))
s_width = float(input('Type in the width of the road section(m): '))
s_thickness = float(input('Type in the thickness of the road surface(cm): '))
s_density = float(input('Type in the density of the road surface(kg per 1 sq.m with 1cm thickness): '))


class Road:
    """
    Класс Road.

    Защищенные атрибуты:
        _length - длинна участка дорожного покрытия
        _width - ширина участка дорожного покрытия
    """
    _length = s_length
    _width = s_width

    def surface_mass(self, _thickness, _density):
        """
        Расчитывает массу необходимого асфальта для дорожного покрытия.

        :param _thickness: Толщина дорожного покрытия;
        :param _density: Плотность асфальта;
        :return: Масса необходимого асфальта
        """
        surface_m = self._width * self._length * _thickness * _density
        return surface_m


road = Road()
print(f'The required mass of asphalt: {road.surface_mass(s_thickness, s_density) / 1000} tons')
