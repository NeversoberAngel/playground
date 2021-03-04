"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.

Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

Программа считает точно по формулам. Без единиц измерения довольно сложно оценить адекватность получаемых цифр.
Хотя, для пошива пальто 62 размера вряд ли понадобится около 10кв.м ткани
(вероятно, все же имеется ввиду размер UK или US, а не EUR)
"""
from abc import ABC, abstractmethod


class SomeClothing(ABC):

    @abstractmethod
    def material_expenditures(self):
        pass


class Clothing(SomeClothing):
    title = 'clothing'
    size = 0
    height = 0
    for_coat = 0
    for_costume = 0
    total = 0

    def __init__(self, v, h):
        self.size = v
        self.height = h

    @property
    def material_expenditures(self):
        self.for_coat = (self.size / 6.5) + 0.5
        self.for_costume = (self.height * 2 / 100) + 0.3
        self.total = round(self.for_coat + self.for_costume, 2)
        return self.total


class Coat(Clothing):
    title = 'coat'

    def __init__(self, v, h):
        super().__init__(v, h)

    @property
    def material_expenditures(self):
        self.for_coat = round((self.size / 6.5) + 0.5, 2)
        return self.for_coat


class Costume(Clothing):
    title = 'costume'

    def __init__(self, v, h):
        super().__init__(v, h)

    @property
    def material_expenditures(self):
        self.for_costume = round((self.height * 2 / 100) + 0.3, 2)
        return self.for_costume


print('\n--------------------------------------------------------------------------------\n')

v_inp = float(input('Type in the size of a person(UK): '))
h_inp = float(input('Type in the height of a person(cm): '))

clothing1 = Clothing(v_inp, h_inp)
coat1 = Coat(v_inp, h_inp)
costume1 = Costume(v_inp, h_inp)

print('')
print(f'Total material for {clothing1.title}: {clothing1.material_expenditures}')
print(f'Material for {coat1.title}: {coat1.material_expenditures}')
print(f'Material for {costume1.title}: {costume1.material_expenditures}')

print('\n--------------------------------------------------------------------------------\n')


