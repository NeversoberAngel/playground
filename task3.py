"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.

Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.

Подсказка: подробный список операторов для перегрузки доступен по ссылке.

В метод make_order не смог обработать случай, когда количества клеток в блоке равны.
Пришлось допрописывать условие в блоке вывода. Если есть идеи, как мне помочь с этим, пожалуйста, подскажите.
"""


class Cell:
    number_of_cells = 0
    sum_of_cells = 0
    subs_of_cells = 0
    mult_of_cells = 0
    div_of_cells = 0
    cells_in_line = 0

    def __init__(self, amount):
        self.number_of_cells = int(amount)

    def __str__(self):
        self.all_cells = f'{"*" * self.number_of_cells}'
        return self.all_cells

    def __add__(self, other):
        self.sum_of_cells = self.number_of_cells + other.number_of_cells
        return Cell(self.sum_of_cells)

    def __sub__(self, other):
        self.subs_of_cells = abs(self.number_of_cells - other.number_of_cells)
        if self.subs_of_cells != 0:
            return Cell(self.subs_of_cells)
        else:
            return f'{dont_know} The blocks are equal!'

    def __mul__(self, other):
        self.mult_of_cells = self.number_of_cells * other.number_of_cells
        return Cell(self.mult_of_cells)

    def __truediv__(self, other):
        if self.number_of_cells >= other.number_of_cells:
            self.div_of_cells = int(self.number_of_cells / other.number_of_cells)
        else:
            self.div_of_cells = int(other.number_of_cells / self.number_of_cells)
        return Cell(self.div_of_cells)

    def make_order(self, quantity):
        output = '\n'.join([self.all_cells[j:j + quantity] for j in range(0, self.number_of_cells, quantity)])
        return output


print('\n--------------------------------------------------------------------------------\n')

dont_know = "¯\_(ツ)_/¯"

n1 = int(input('Type in the number of cells in the first block: '))
n2 = int(input('Type in the number of cells in the second block: '))

out1 = Cell(n1)
out2 = Cell(n2)

o_sum_cells = out1 + out2
o_sub_cells = out1 - out2
o_mult_cells = out1 * out2
o_div_cells = out1 / out2

print(f'\nHere is your first block: \n{out1}')
print(f'\nHere is your second block: \n{out2}')
print(f'\nBlocks together: \n{o_sum_cells}')
print(f'\nThe difference in the amounts of cells in blocks: \n{o_sub_cells}')
print(f'\nCells of one block multiplied by cells in another block: \n{o_mult_cells}')
print(f'\nThis many full times one block of cells is larger than another: \n{o_div_cells}')

print(f'\nSeems there are too many cells to display in one line. Let us fragment them.')
q = int(input('Type in the number of cells to display in each line: '))

print(f'\nHere is your first block: \n{out1.make_order(q)}')
print(f'\nHere is your second block: \n{out2.make_order(q)}')
print(f'\nBlocks together: \n{o_sum_cells.make_order(q)}')
print(f'\nThe difference in the amounts of cells in blocks: '
      f'\n{o_sub_cells.make_order(q)if n1 != n2 else o_sub_cells}')
print(f'\nCells of one block multiplied by cells in another block: \n{o_mult_cells.make_order(q)}')
print(f'\nThis many full times one block of cells is larger than another: \n{o_div_cells.make_order(q)}')

print('\n--------------------------------------------------------------------------------\n')
