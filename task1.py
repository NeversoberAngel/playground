"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.

Реализован счетчик секунд до переключения.
Про усложнение задачи, а конкретно - про проверку порядка режимов - я совсем не понял.
Буду ждать разбора ДЗ.
"""

from time import sleep


class TrafficLight:
    """
    Класс TrafficLight. Атрибут класса - __color - приватный.
    """
    __color = ('Red', 'Yellow', 'Green')

    def running(self, m=0, start_new_cycle='y'):
        """
        Переключает сигналы светофора в установленном порядке Красный - Желтый - зеленый.
        По завершении предлагает запустить цикл снова.

        :param m: Счетчик переключений светофора;
        :param start_new_cycle: Условие для запуска нового цикла;
        :return: Цикл переключений сигналов светофора.
        """

        while start_new_cycle == 'y' or start_new_cycle == 'Y':
            while m < 3:
                output = self.__color[m]
                print(f'Current color is: ', end='')
                if self.__color[m] == 'Red':
                    print(f'\033[31m{output}\033[0m', end='')
                    for i in range(0, 7):
                        print(f' {7 - i}', end='')
                        sleep(1)
                    print(' >>>')
                    m += 1
                elif self.__color[m] == 'Yellow':
                    print(f'\033[33m{output}\033[0m', end='')
                    for i in range(0, 2):
                        print(f' {2 - i}', end='')
                        sleep(1)
                    print(' >>>')
                    m += 1
                elif self.__color[m] == 'Green':
                    print(f'\033[32m{output}\033[0m', end='')
                    for i in range(0, 5):
                        print(f' {5 - i}', end='')
                        sleep(1)
                    print(' >>>')
                    m += 1
            print('The traffic light has stopped!')
            start_new_cycle = input('Do you want to run cycle one more time(y/n)? ')
            if start_new_cycle == 'y' or start_new_cycle == 'Y': m = 0


traffic_light = TrafficLight()
traffic_light.running()
