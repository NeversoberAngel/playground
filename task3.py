"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

На выводе прибавились: сам файл, вместо фамилии - имя и фамилия.
"""

salary = open('names-salary.txt')
salary_text = salary.read()
print(f'\n{salary_text}')
salary.seek(0)
salary_list = salary.readlines()
salary.seek(0)
salary_total = 0
employees_with_salary_less_than_20000 = []
for each_line in salary_list:
    salary_list_line = salary.readline()
    salary_list_items = salary_list_line.split('\t')
    if salary_list_items[-2] == 'Salary':
        continue
    salary_list_items[-2] = int(salary_list_items[-2])
    salary_total += salary_list_items[-2]
    if salary_list_items[-2] < 20000:
        employees_with_salary_less_than_20000.append(f'{salary_list_items[0]} {salary_list_items[-4]}')

employees_with_salary_less_than_20000_line = ', '.join(employees_with_salary_less_than_20000)

print(f'\nThe following employees have salary less than 20000 Cr: {employees_with_salary_less_than_20000_line}')
print(f'\nAverage salary is: {round(salary_total / (len(salary_list) - 1))} Cr')

salary.close()
