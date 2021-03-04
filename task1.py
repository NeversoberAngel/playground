"""
1. Реализовать класс Matrix (матрица).

Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

Программа заправшивает размеры матриц, которые необходимо сложить.
Затем генерирует случайные матрицы.
"""
from random import randrange

print('\n--------------------------------------------------------------------------------\n')

rows = int(input(f'Type in the number of the matrix rows: '))
lines = int(input(f'Type in the number of the matrix lines: '))

mat1 = [[randrange(-99, 99) for j in range(rows)] for i in range(lines)]
mat2 = [[randrange(-99, 99) for j in range(rows)] for i in range(lines)]
mat3 = [[randrange(-99, 99) for j in range(rows)] for i in range(lines)]


class Matrix:
    matrix = []

    def __init__(self, mat):
        self.matrix = mat

    def __str__(self):
        output = '\n'.join(''.join(f'{self.matrix[i][j]:5}' for j in range(rows)) for i in range(lines))
        return output

    def __add__(self, other):
        sum_of_m = [[(self.matrix[i][j] + other.matrix[i][j]) for j in range(rows)] for i in range(lines)]
        return Matrix(sum_of_m)


m1 = Matrix(mat1)
print(f'\nMatrix 1: \n{m1}')

m2 = Matrix(mat2)
print(f'\nMatrix 2: \n{m2}')

m3 = Matrix(mat3)
print(f'\nMatrix 3: \n{m3}')

print(f'\nThe sum of all matrices is: \n{m1 + m2 + m3}\n')
print('--------------------------------------------------------------------------------')
