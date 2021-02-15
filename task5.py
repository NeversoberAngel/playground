"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().

!!! Как переносить элементы списка бесчестно взял в интернете(сам поленился сделать).
Как переносить текст тоже подсмотрел в интернете.
"""

from functools import reduce
from auxilary import multiplication, list_wrapper
from textwrap import fill

original_list = [el for el in range(100, 1001) if el % 2 == 0]

print('\nOriginal list:\n' + str(list_wrapper(original_list, 40)))
print('\nMultiplication of all the elements in list:\n' + fill(str(reduce(multiplication, original_list)), width = 159))
