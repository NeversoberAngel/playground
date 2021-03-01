"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Проверить работу примера, создав экземпляр и вызвав описанный метод.

!!!Данный скрипт следует запускать в Windows через cmd.!!!

Позволяет производить настройку продолжительности каждого из согналов светофора.

Скрипт переключает цвета светофора, как это происходит на практике в реальной жизни:
После красного перед зеленым включается двойной сигнал: красный и желтый.
После зеленого - сначала желтый, затем красный.

Прерывания выполняется любой клавишей - завершается текущее переключение и выводится сообщение.
"""

from time import sleep
from os import system
from msvcrt import kbhit

system('cls')

r = int(input('Type in the duration of \033[31mRed\033[0m signal: '))
y = int(input('Type in the duration of \033[33mYellow\033[0m signal: '))
g = int(input('Type in the duration of \033[32mGreen\033[0m signal: '))

system('cls')


class TrafficLight:
    """
    Класс TrafficLight. Атрибут класса - __color - приватный.
    """
    __color = ('Red', 'Yellow', 'Green')

    def running(self, m=0, duretion_red=r, duretion_yellow=y, duretion_green=g):
        """
        Переключает сигналы светофора в том порядке, в каком это происходит в реальности(в РФ):
        ... - Красный - Красный и Желтый - Зеленый - Желтый - Красный - ...

        Условие для прерывания выполнения программы - нажатие любой клавиши.
        Текущее переключение доходит до конца и скрипт завершается.

        :param m: Индекс сигнала светофора;
        :param duretion_red: Продолжительность красного сигнала;
        :param duretion_yellow: Продолжительность желтого сигнала;
        :param duretion_green: Продолжительность зеленого сигнала;
        :return: Переключений сигналов светофора.
        """

        while not kbhit():
            output = self.__color[m]
            if self.__color[m] == 'Red':
                for i in range(0, duretion_red):
                    print(f'Current color is: \033[31m{output}\033[0m {duretion_red - i}..')
                    sleep(1)
                    system('cls')
                m += 1
            elif self.__color[m] == 'Yellow':
                for i in range(0, duretion_yellow):
                    print(f'Current color is: \033[31m{self.__color[m - 1]}\033[0m')
                    print(f'Current color is: \033[33m{output}\033[0m {duretion_yellow - i}..')
                    sleep(1)
                    system('cls')
                m += 1
            elif self.__color[m] == 'Green':
                for i in range(0, duretion_green):
                    print(f'Current color is: \033[32m{output}\033[0m {duretion_green - i}..')
                    sleep(1)
                    system('cls')
                m -= 1
                if kbhit():
                    break
                if self.__color[m] == 'Yellow':
                    output = self.__color[m]
                    for i in range(0, duretion_yellow):
                        print(f'Current color is: \033[33m{output}\033[0m {duretion_yellow - i}..')
                        sleep(1)
                        system('cls')
                    m -= 1
        print('The traffic light was stopped.')


traffic_light = TrafficLight()
traffic_light.running()
