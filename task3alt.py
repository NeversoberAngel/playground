f_name = []
l_name = []
w_pos = []
income = []

with open('workersList.txt') as workers_list:
    workers_aux = workers_list.readlines()
    workers_list.seek(0)
    for each_line in workers_aux:
        workers_lines = workers_list.readline()
        workers_line = workers_lines.split(' ')
        if workers_line[0] == 'Name':
            continue
        f_name.append(workers_line[0])
        l_name.append(workers_line[1])
        w_pos.append(workers_line[2])
        income.append({'salary': float(workers_line[3]), 'bonus': float(workers_line[4])})


class Worker:
    """
    Класс Worker.

    Атрибуты:
        name - Столбец с именами сотрудников;
        surname - Столбец с фамилиями сотрудников;
        position - Столбец с должностями сотрудников;
        _income - Столбцы окладов и бонусов сотрудников.
    """
    name = f_name
    surname = l_name
    position = w_pos
    _income = income


class Position(Worker):
    """
    Класс Position. Родительский класс для данного класса - Worker.

    Атрибуты: унаследованы от родительского класса.
    """

    def get_each_worker_data(self):
        """
        Возвращает данные об именах сотрудников и их общих доходах.

        :return: Вывод на экран Имени, Фамилии, суммы оклада и премии каждого сотрудника.
        """
        for i in range(len(f_name)):
            w_inc = self._income[i]
            w_sal = w_inc.get('salary')
            w_bon = w_inc.get('bonus')
            print(f"\nThe worker's full name is: {self.name[i]} {self.surname[i]}")
            print(f"The worker's total income is: {w_sal + w_bon}")
        pass


position = Position()
position.get_each_worker_data()
