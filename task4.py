"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

К сожалению, не разобрался, как можно воспользоваться возможностями словаря :(((
"""

en_to_ru = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
en2ru = ['Один', 'Два', 'Три', 'Четыре']

numbers_text = open('numbers.txt', 'r', encoding='UTF-8')
numbers_text_lines = numbers_text.readlines()
subst_numbers_line_list = []
numbers_text.seek(0)
for each_line in range(len(numbers_text_lines)):
    numbers_line = numbers_text.readline()
    numbers_line_items = numbers_line.split(' ')
    numbers_line_items[0] = en2ru[each_line]
    subst_numbers_line = ' '.join(numbers_line_items)
    subst_numbers_line_list.append(subst_numbers_line)
numbers_text.close()

ru_numbers_text = open('ru_numbers.txt', 'w', encoding='UTF-8')
ru_numbers_text.writelines(subst_numbers_line_list)
ru_numbers_text.close()