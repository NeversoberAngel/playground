"""
Программа возводит действительное число в отрицательную степень с использованием функции pow.
"""

"""Задаем значения для основания и покателя степени с типом Null, для проверки на пустые вводимые значение"""
x = None
y = None

"Исключение 'пустых' значений для основания и показателя степени"
while x is None:
    try:
        x = float(input('Введите число, которое нужно возвести в степень: '))
    except ValueError:
        print('Число не введено')

while y is None:
    try:
        y = int(input('Введите степень, в которую нужно возвести число: '))
    except ValueError:
        print('Степень не введена')


def exponentiation(a1, a2):
    """
    Функция возводит число в степень

    :param a1: основание степени
    :param a2: показатель степени
    :return: вывод на экран числа в степени
    """
    return print('Результат: ', pow(a1, a2))


"""Вывод результата"""
exponentiation(x, y)
