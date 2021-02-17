"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

Предусмотрен случай, когда ввад пользователя заканчивается пробелом. Только запись в файл происходит в конце.
"""
sum_users_input_numbers = 0
users_numbers = input('Type in several numbers to count a sum of them: ')
users_numbers_list = users_numbers.split(' ')
if users_numbers_list[-1] == '':
    users_numbers_list.pop(-1)
try:
    for each_number in range(len(users_numbers_list)):
        users_numbers_list[each_number] = float(users_numbers_list[each_number])
    for each_in_sum in range(len(users_numbers_list)):
        sum_users_input_numbers += users_numbers_list[each_in_sum]
    print('The result is: ', sum_users_input_numbers)
except ValueError:
    print('Seems you have entered not numbers.')

users_numbers_input = open('users_input_numbers_alt.txt', 'w')
users_numbers_input.write(users_numbers)
users_numbers_input.close()
