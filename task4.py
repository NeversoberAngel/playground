"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

Было желание значительно доработать скрипт, как-то доработать недописанные методы,
назначить одинаковый цвет всем полицейским автомобилям, но не успеваю.
Оставлю скрипт себе для практики в кодировании.
"""

from random import randrange

# списки для генерации атрибутов классов
car_types = ['town car', 'sport car', 'work car', 'police car']
car_colors = ['\x1b[37mwhite\x1b[0m', '\x1b[30mgrey\x1b[0m', '\x1b[31mred\x1b[0m', '\x1b[33myellow\x1b[0m',
              '\x1b[32mgreen\x1b[0m', '\x1b[34mblue\x1b[0m', '\x1b[35mmagenta\x1b[0m', '\x1b[36mcyan\x1b[0m']
car_names = ['Saab', 'Mitsubishi', 'Mercedes', "Honda", 'Chevrolet', 'Nissan', 'Volvo', 'Lamborghini', 'Fiat',
             'Bugatti', 'Audi', 'Lada', 'Skoda', 'DeLorean']
if_police = [False, False, False, False, False, False, False, True]
if_on_race = [False, False, False, True]
if_on_chase = [False, False, False, True]

# Ввод количества машин и количества пар действий (движение-поворот)
d = int(input('\nType in the number of cars to display: '))
c = int(input('\nType in the number of actions to display: '))


class Car:
    """
    Класс Car.

    Атрибуты публичные:
        speed - скорость;
        color - цвет автомобиля;
        name - марка автомобиля;
        is_police - принадлежность автомобиля к ООП(органам охраны правопорядка,
                    не путать с объектно-ориентированным программированием)
    """
    speed = 'default'
    color = 'default'
    name = 'default'
    is_police = 'default'

    def __init__(self):
        """
        Конструктор класса. При вызове класса формируются следующие атрибуты:

        self.car_type - случайным образом из списка выбирается тип автомобиля;
        self.color - случайным образом из списка выбирается цвет автомобиля;
        self.name - случайным образом из списка выбирается марка автомобиля;
        self.is_police - случайным образом из списка выбирается прпинадлежность автомобиля к полиции;
        self.speed - случайным образом выбирается число от -20 до 180 с шагом в 20
                    (критерии выбораны с целью проверки достоверности исполняемого кода.).
        """
        self.car_type = car_types[randrange(len(car_types))]
        self.color = car_colors[randrange(len(car_colors))]
        self.name = car_names[randrange(len(car_names))]
        self.is_police = if_police[randrange(len(if_police))]
        self.speed = randrange(-20, 180, 20)

    def go(self):
        """
        Метод go класса Car. Показывает направление движения автомобиля, расстояние,
        пройденное автомобилем.

        Внутри метода определяется:
            distance - расстояние, пройденное автомобилем

        В зависимости от скорости определяется движется ли автомобиль вперед или назад.
        При нулевой скорости вызывается метод stop('Остановка автомобиля')

        :return: блоки текста:
                напрвление движения автомоблия,
                пройденное автомобилем расстояние.
        """
        distance = randrange(10, 200, 10)
        if self.speed != 0:
            if self.speed > 0:
                go_output = f' forward'
            else:
                go_output = f' backward'
            return f' moved{go_output} {distance}m'
        else:
            return self.stop()

    def stop(self):
        """
        Метод stop класса Car. Индикатор того,что автомобиль не движется.
        Вызывается методом go, если скорость движения автомобиля равна нулю.

        :return: При вызове метода появляется блок текста, информирующий об отсутствии движения автомобиля.
        """
        stop_output = f' stopped'
        return stop_output

    def turn(self):
        """
        Метод go класса Car. Показывает направление движения автомобиля, расстояние,
        пройденное автомобилем.

        Внутри метода определяется:
            direction - направление поворота автомобиля в градусах.
                        Случайным образом выбирается число от -180 до 180 с шагом в 90.
                        (критерии выбораны с целью проверки достоверности исполняемого кода.).

        В зависимости от угла поворота определяется поворачивает ли автомобиль направо или налево,
        разворачивается, или не меняет направление движения.

        :return: Блок текста:
                Направление поворота и угол поворота в градусах.
        """
        direction = randrange(-180, 180, 90)
        if direction != 0:
            if direction in (-180, 180):
                turn_output = f' turned around;'
            elif direction < 0:
                turn_output = f' turned left {abs(direction)}deg;'
            else:
                turn_output = f' turned right {direction}deg;'
            return turn_output
        else:
            return f' moved straight;'

    def show_speed(self):
        """
        Метод show_speed класса Car. При вызове метода показывается скорость автомобиля.

        :return: Блок текста со скоростью автомобиля.
        """

        show_speed_output = f' at {abs(self.speed)}kmph;'
        return show_speed_output


class TownCar(Car):
    """
    Класс TownCar. Дочерний класс класса Car.

    Атрибут публичный:
        speed_limit - предел допустимой скорости для данного класса автомобилей.
    """
    speed_limit = 60

    def __init__(self):
        """
        Конструктор класса.

        Все атрибуты наследуются от ролдительского класса.
        """
        super(TownCar, self).__init__()

    def show_speed(self):
        """
        Метод show_speed класса TownCar. Переопределенный метод класса Car.
        При вызове метода показывается скорость автомобиля,
        а также в случае превышения допустимой скорости, выводится соответствующее сообщениею

        :return: Блок текста со скоростью автомобиля, и сопктствующим сообщением.
        """

        if self.speed > self.speed_limit:
            show_speed_output = f' at {abs(self.speed)}kmph \033[31m(the speed is too high: ' \
                                f'{self.speed - self.speed_limit}kmph above limit)\033[0m;'
        else:
            show_speed_output = f' at {abs(self.speed)}kmph \033[32m(no rules violated)\033[0m;'
        return show_speed_output


class SportCar(Car):
    """
    Класс SportCar. Дочерний класс класса Car.

    Атрибут публичный:
        is_on_race - показывает, участвует ли данный автомобиль в гонке.
    """
    is_on_race = 'default'

    def __init__(self):
        """
        Конструктор класса.

        Все атрибуты наследуются от ролдительского класса.
        self.is_on_race - случайным образом из списка выбирается значение для того,
                        участвует автомобиль в гонке или нет.
        """
        super(SportCar, self).__init__()
        self.is_on_race = if_on_race[randrange(len(if_on_race))]

    def on_race(self):
        """
        !!! Метод не дописан и не вызывается при выводе(пока не доработан) !!!

        Метод on_race класса SportCar.
        В случае, если автомобиль находится на гонке - выводится соответствующее сообщение
        и контроля скорости не осуществляется. в противном случае вызывается метод show_speed
        класса TownCar.

        :return: Блок текста с соответствующим сообщением или переопределенный для TownCar метод show_speed.
        """
        if self.is_on_race:
            on_race_output = f' the car is on race'
            return on_race_output
        else:
            TownCar.show_speed(self)


class WorkCar(Car):
    """
    Класс WorkCar. Дочерний класс класса Car.

    Атрибут публичный:
        speed_limit - предел допустимой скорости для данного класса автомобилей.
    """

    speed_limit = 40

    def __init__(self):
        """
        Конструктор класса.

        Все атрибуты наследуются от ролдительского класса.
        """
        super(WorkCar, self).__init__()

    def show_speed(self):
        """
        Метод show_speed класса WorkCar. Переопределенный метод класса Car.
        При вызове метода показывается скорость автомобиля,
        а также в случае превышения допустимой скорости, выводится соответствующее сообщениею

        :return: Блок текста со скоростью автомобиля, и сопктствующим сообщением.
        """
        if self.speed > self.speed_limit:
            show_speed_output = f' at {abs(self.speed)}kmph \033[31m(the speed is too high:' \
                                f' {self.speed - self.speed_limit}kmph above limit)\033[0m;'
        else:
            show_speed_output = f' at {abs(self.speed)}kmph \033[32m(no rules violated)\033[0m;'
        return show_speed_output


class PoliceCar(Car):
    """
    Класс PoliceCar. Дочерний класс класса Car.

    Атрибут публичный:
        is_on_chase - показывает, находится ли данный автомобиль в погоне или нет.
    """
    is_on_chase = 'default'

    def __init__(self):
        """
        Конструктор класса.

        Все атрибуты наследуются от ролдительского класса.
        self.is_on_chase - случайным образом из списка выбирается значение для того,
                        участвует d погоне или нет.
        self.car_type - назначается тип 'police car', если значение is_police = True
        self.is_police - назначается значение is_police = True, если тип автомобиля 'police car'
        """

        super(PoliceCar, self).__init__()
        if self.car_type == 'police car' or self.is_police:
            self.car_type = 'police car'
            self.is_police = True
        else:
            pass

    def police_warning(self):
        """
        Сообщение о том, является автомобиль полицейским или гражданским.

        :return: блок текста, идентифицирующий автомобиль как полицейский или гражданский.
        """
        if self.is_police:
            police_warning_output = f'\x1b[34m!!!POL\x1b[0m\x1b[31mICE!!!\x1b[0m'
        else:
            police_warning_output = f'\x1b[37mCIVIL\x1b[0m'
        return police_warning_output

    def on_chase(self):
        """
        !!! Метод не дописан и не вызывается при выводе(пока не доработан) !!!

        Метод on_chase класса PoliceCar.
        В случае, если автомобиль находится в погоне - выводится соответствующее сообщение
        и контроля скорости не осуществляется. в противном случае вызывается метод show_speed
        класса TownCar.

        :return: Блок текста с соответствующим сообщением или переопределенный для TownCar метод show_speed.
        """
        if self.is_on_chase:
            on_race_output = f' the car is on chase'
            return on_race_output
        else:
            WorkCar.show_speed(self)


# Вывод значений. Вызываются классы, методы классов. Тип автомобиля выводится через класс PoliceCar,
# поскольку в не приведены в соответствие параметры is_police и car_type = 'police car'
for q in range(d):
    car_details = Car()
    police_car = PoliceCar()
    print(
        f'\n{q + 1}. {police_car.police_warning()}  {c} '
        f'actions for {police_car.car_type} {car_details.color} {car_details.name}: ')
    for r in range(c):
        work_car = WorkCar()
        town_car = TownCar()
        car_actions = Car()
        if police_car.car_type == 'town car':
            print(f'\t{r + 1}.{town_car.go()}{town_car.show_speed()}{town_car.turn()}')
        elif police_car.car_type == 'work car':
            print(f'\t{r + 1}.{work_car.go()}{work_car.show_speed()}{work_car.turn()}')
        else:
            print(f'\t{r + 1}.{car_actions.go()}{car_actions.show_speed()}{car_actions.turn()}')
