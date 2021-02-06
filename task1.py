"""
Программа делит одно число на другое.
"""

"""Задаем значения для делимого и делителя с типом Null, для проверки на пустые вводимые значение"""
a = None
b = None

"Исключение 'пустых' значений для делимого иделителя"
while a is None:
    try:
        a = int(input('Введите делимое: '))
    except ValueError:
        print('Делимое не введено')

while b is None:
    try:
        b = int(input('Введите делитель: '))
    except ValueError:
        print('Делитель не введен')


def division(dividend, divisor):
    """
    Функция возвращает результат деления одного числа на другое

    :param dividend: делимое
    :param divisor: делитель
    :return: вывод на экран частного
    """
    try:
        return print('Частное равно: ', dividend / divisor)
    except ZeroDivisionError:
        return print('И как прикажете делить на ноль?')


"""Вывод результата"""
division(a, b)
