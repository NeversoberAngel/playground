"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class CustomException:
    elements_list = []

    def __init__(self):
        self.list_builder()

    @classmethod
    def list_builder(cls, input_data=''):
        counter = 1
        while input_data != 'stop':
            input_data = input(f"Type in the element #{counter} or 'stop' to finish input: ")
            try:
                input_data = float(input_data)
                cls.elements_list.append(input_data)
                counter += 1
            except ValueError:
                cls.validator(input_data)

    @staticmethod
    def validator(inp):
        try:
            float(inp)
        except ValueError:
            if inp == 'stop':
                pass
            else:
                print(f"\033[31m'{inp}' is not a number\033[0m")

    def __str__(self):
        return f'\nNumbers list: \n{self.elements_list}'


out = CustomException()
print(out)

