"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = 'default'

    def __init__(self):
        self.title = f'Канцелярские принадлежности'

    def draw(self):
        draw_output = 'Запуск отрисовки'
        return draw_output


class Pen(Stationery):

    def __init__(self):
        super().__init__()
        self.title = f'Ручка'

    def draw(self):
        draw_output = 'Запуск отрисовки ручкой'
        return draw_output


class Pencil(Stationery):

    def __init__(self):
        super().__init__()
        self.title = f'Карандаш'

    def draw(self):
        draw_output = 'Запуск отрисовки карандашом'
        return draw_output


class Handle(Stationery):

    def __init__(self):
        super().__init__()
        self.title = f'Маркер'

    def draw(self):
        draw_output = 'Запуск отрисовки маркером'
        return draw_output


stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

print(f'\n{stationery.title}')
print(f'{stationery.draw()}')
print(f'\n{pen.title}')
print(f'{pen.draw()}')
print(f'\n{pencil.title}')
print(f'{pencil.draw()}')
print(f'\n{handle.title}')
print(f'{handle.draw()}')
