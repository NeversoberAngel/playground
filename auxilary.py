"""
Библиотека функций, которые будут использованы в ходе выполнения домашнего задания
"""


def rand_num_list(first_element, last_element, number_of_elements):
    """
    The script returns a given number of integer elements in a given range

    :param first_element: Start of range
    :param last_element: End of range
    :param number_of_elements: Number of elements
    :return: The list with random integer elements
    """
    from random import randint
    result_list = [randint(first_element, last_element) for rand_n in range(number_of_elements)]
    return result_list


def multiplication(elem, factor):
    """
    Simple multiplication. Auxilary for Task5

    :param elem: Element to multiply
    :param factor: Factor
    :return: Result of multiplication
    """
    moaeil = elem * factor
    return moaeil


def list_wrapper(list_to_wrap, items_per_line):
    """
    Wraps list into lines with a defined amount of elements.

    :param list_to_wrap: List to wrap
    :param items_per_line: Number of items in one line
    :return: Wrapped list
    """
    lines = []
    for i in range(0, len(list_to_wrap), items_per_line):
        piece_of_list = list_to_wrap[i:i + items_per_line]
        line = ' '.join('{!r}'.format(x) for x in piece_of_list)
        lines.append(line)
    return "\n".join(lines)


def list_builder(first_element, last_element):
    """
    Builds a list of integer elements

    :param first_element: First element
    :param last_element: Last element
    :return: List of integer elements
    """
    from itertools import count
    result_list = []
    for el in count(first_element):
        result_list.append(el)
        if el >= last_element:
            break
    return result_list


def list_dublicator(initial_list, number_of_elements):
    """
    Repeats a specific number of list items

    :param initial_list: Initial list of items
    :param number_of_elements: Number of items to show
    :return: Requested list of items
    """
    from itertools import cycle
    dubl_list = []
    c = 1
    for el in cycle(initial_list):
        dubl_list.append(el)
        if c >= number_of_elements:
            break
        c += 1
    return dubl_list


def fact(n):
    """
    Auxilary function for Task7

    :param n: Number of elements to show
    :return: Factorial of numbers from 1 to n
    """
    from math import factorial
    for elem in range(1, n + 1):
        yield factorial(elem)

