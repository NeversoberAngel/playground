"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

project = 'Operations with complex numbers'


class ComplexNumber:

    def __init__(self, real_part, imaginary_part):
        self.real = real_part
        self.imaginary = imaginary_part

    def __str__(self):
        if self.imaginary == 1:
            self.complex_number = f'{self.real} + i'
        elif self.imaginary == -1:
            self.complex_number = f'{self.real} - i'
        elif self.imaginary < 0:
            self.complex_number = f'{self.real} - {abs(self.imaginary)}i'
        else:
            self.complex_number = f'{self.real} + {self.imaginary}i'
        return self.complex_number

    def __add__(self, other):
        self.sum_real = self.real + other.real
        self.sum_imaginary = self.imaginary + other.imaginary
        return ComplexNumber(self.sum_real, self.sum_imaginary)

    def __mul__(self, other):
        self.mult_real = self.real * other.real - (self.imaginary * other.imaginary)
        self.mult_imaginary = (self.real * other.imaginary) + (self.imaginary * other.real)
        return ComplexNumber(self.mult_real, self.mult_imaginary)


def tidying_up(list_input):
    list_input = list_input.split(' ')
    list_input = list(filter(None, list_input))
    list_input[0] = int(list_input[0])
    list_input[1] = int(list_input[1])
    return list_input


c1 = input('type in the real and imaginary part of the first complex number separated by space and press Enter: ')
c2 = input('type in the real and imaginary part of the second complex number separated by space and press Enter: ')
c1 = tidying_up(c1)
c2 = tidying_up(c2)
c1 = ComplexNumber(c1[0], c1[1])
c2 = ComplexNumber(c2[0], c2[1])
print(f'\nthe first complex number is: {c1}')
print(f'the second complex number is: {c2}')
print(f'\nthe sum of the complex numbers is: {c1 + c2}')
print(f'the product of the complex numbers is: {c1 * c2}')
