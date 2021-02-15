"""
2. Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

from auxilary import rand_num_list

fel = int(input('Type the first element in the list: '))
lel = int(input('Type in the last element in the list: '))
noel = int(input('Type in the number of elements: '))
original_list = rand_num_list(fel, lel, noel)

print(f'\nOriginal list: {original_list}')
print(f'\nSolution(the current element is bigger than the previous one): {[original_list[i + 1] for i in range(0, len(original_list) - 1) if original_list[i] < original_list[i + 1]]}')
