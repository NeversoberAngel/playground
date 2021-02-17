"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

Также реализована возможность ввода текста Кириллицей.
"""

users_input_file = open('users_input_file.txt', 'w', encoding='utf-8')
users_text = input('Please type in the text you want to see in your file: ')
while True:
    users_input_file.writelines(f'{users_text}\n')
    users_text = input()
    if not users_text:
        break
users_input_file.close()
