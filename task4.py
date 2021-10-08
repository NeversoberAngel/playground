"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

from auxilary import rand_num_list

fel = int(input('Type the first element in the list: '))
lel = int(input('Type in the last element in the list: '))
noel = int(input('Type in the number of elements: '))
original_list = rand_num_list(fel, lel, noel)

print(f'\nOriginal list: {original_list}')
print(f'\nSolution(only non-repeating elements): {[el for el in original_list if original_list.count(el) == 1]}')
