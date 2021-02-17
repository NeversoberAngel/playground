"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

Хотел сделать форматирование вывода Initial data, чтобы автоматически подтягивалась строка:
row1, row2, row3, row4, row5 = [each_activity_houring[0], each_activity_houring[1], each_activity_houring[2],
                                        each_activity_houring[3], each_activity_houring[4]]
"""

from re import findall

print('\nInitial data:')

with open('courses.txt', 'r') as courses:
    courses_lines = courses.readlines()
    courses.seek(0)
    courses_houring_dict = {}
    for each_line in range(len(courses_lines)):
        courses_line = courses.readline()
        courses_houring = courses_line.split('\n')
        each_activity = courses_houring[0]
        each_activity = each_activity.replace("\t", " ")
        each_activity_houring = each_activity.split(' ')
        each_activity_houring = [i for i in each_activity_houring if i != '']
        sum_of_hours = 0
        for each_line in range(len(each_activity_houring)):
            hours = findall(r'\d+', str(each_activity_houring[each_line]))
            hours = [int(hours_val) for hours_val in hours]
            if hours is None:
                continue
            for each_line in range(len(hours)):
                sum_of_hours += hours[each_line]
        courses_houring_dict.update({each_activity_houring[each_line]: sum_of_hours})

        row1, row2, row3, row4, row5 = [each_activity_houring[0], each_activity_houring[1], each_activity_houring[2],
                                        each_activity_houring[3], each_activity_houring[4]]
        print(f"{row1:<18} {row2:>12} {row3:>12} {row4:>12} {row5:>12}")

print(f'\nRequested dictionary:\n{courses_houring_dict}')
