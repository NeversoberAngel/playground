"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class CustomError(Exception):
    err_text = ''

    def __init__(self, err_text):
        self.error_text = err_text


class CustomOperations:

    def __init__(self, variab):
        try:
            self.op_vars = float(variab)
        except ValueError:
            self.op_vars = ''

    def __str__(self):
        return f'{self.op_vars}'

    def __truediv__(self, other):
        try:
            dvnd = float(self.op_vars)
            dvsr = float(other.op_vars)
            if dvsr == 0:
                raise CustomError('Division by zero is forbidden')
            return CustomOperations(dvnd / dvsr)
        except ValueError:
            raise CustomError('Cannot proceed the operation on this data type.')


try:
    dividend = CustomOperations(input('Type in the dividend: '))
    divisor = CustomOperations(input('Type in the divisor: '))
    quotient = dividend / divisor
    print(quotient)
except CustomError as zderr:
    print(zderr)
