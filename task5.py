"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

Не смог предусмотреть, когда ввод заканчивается пробелом
"""

users_numbers_input = open('users_input_numbers.txt', 'w')
users_numbers = input('Type in several numbers to count a sum of them: ').split(' ')
users_numbers_input.write(' '.join(users_numbers))
sum_users_input_numbers = 0
try:
    for each_number in range(len(users_numbers)):
        users_numbers[each_number] = float(users_numbers[each_number])
    for each_in_sum in range(len(users_numbers)):
        sum_users_input_numbers += users_numbers[each_in_sum]
    print('The result is: ', sum_users_input_numbers)
except ValueError:
    print('Seems you have entered not numbers, or finished input with space.')
users_numbers_input.close()
