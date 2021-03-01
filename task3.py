"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""

f_name = 'John'
l_name = 'Snow'
w_pos = 'Crow'
salary = 10000
bonus = 1000


class Worker:
    """
    Класс Worker.

    Атрибуты:
        name - Имя;
        surname - Фамилия;
        position - Должность;
        _income - оклад и бонус.
    """
    name = f_name
    surname = l_name
    position = w_pos
    _income = {'salary': salary, 'bonus': bonus}


class Position(Worker):
    """
    Класс Position. Родительский класс для данного класса - Worker.

    Атрибуты: унаследованы от родительского класса.
    """

    def get_full_name(self):
        """
        Получение Имени и фамилии работника

        :return: Вывод на экран имени и фамилии работника
        """
        return f"The worker's full name is: {self.name} {self.surname}"

    def get_total_income(self):
        """
        Получение значения общего дохода сотрудника

        :return: Вывод на экран полного дохода сотрудника
        """
        w_inc = self._income
        w_sal = w_inc.get('salary')
        w_bon = w_inc.get('bonus')
        return f"The worker's total income is: {w_sal + w_bon}"


position = Position()

full_name = position.get_full_name()
total_income = position.get_total_income()

print(f'{full_name}\n{total_income}')
