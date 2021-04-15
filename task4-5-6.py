"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""

"""
Проект "Склад оргтехники"
"""

project_name = "Warehouse"


class ActionUnavailable(Exception):
    err_text = "\033[31mError: action unavailable\033[0m"

    def __init__(self):
        print(self.err_text)
        Warehouse.warehouse_management()


class NoEquipmentToTransfer(Exception):
    err_text = '\033[31mError: There is no equipment to transfer\033[0m'

    def __init__(self):
        print(self.err_text)


class NoEquipmentToWriteOff(Exception):
    err_text = '\033[31mError: There is no equipment to write-off\033[0m'

    def __init__(self):
        print(self.err_text)
        Warehouse.warehouse_management()


class WrongEqNumber(Exception):
    err_text = '\033[31mError: wrong equipment number\033[0m'

    def __init__(self, redirect):
        print(self.err_text)
        if redirect == 'assign_to':
            Warehouse.assign_to()
        else:
            Warehouse.write_off()
        Warehouse.warehouse_management()


class WrongCharacteristics(Exception):
    err_text = '\033[31mError: Some of the characteristics are odd or missing\033[0m'

    def __init__(self):
        print(self.err_text)
        Warehouse.warehouse_management()


class WrongPrice(Exception):
    err_text = '\033[31mError: price must be a positive number\033[0m'

    def __init__(self):
        print(self.err_text)
        Warehouse.warehouse_management()


class WrongAmount(Exception):
    err_text = '\033[31mError: amount must be a positive integer\033[0m'

    def __init__(self):
        print(self.err_text)
        Warehouse.warehouse_management()


class Warehouse:
    in_stock = {}
    inv = 0
    inv_n = ''
    assigned_to = 'warehouse'
    inp_action = 'start'

    @classmethod
    def warehouse_management(cls):
        while True:
            cls.inp_action = input("\ntype in the action for equipment:"
                                   "\n\t'accept' - to accept equipment to warehouse;"
                                   "\n\t'transfer' - to transfer equipment to department;"
                                   "\n\t'off' - to write the equipment off"
                                   "\n\t'stop' - to finish the script"
                                   "\naction: ")
            inp_action = Warehouse.action_validator(cls.inp_action)
            if inp_action == "ACCEPT":
                Warehouse.accept()
            elif inp_action == "TRANSFER":
                Warehouse.assign_to()
            elif inp_action == 'OFF':
                Warehouse.write_off()
            elif inp_action == 'STOP':
                break
            else:
                pass
        Warehouse.finish_script()

    @staticmethod
    def action_validator(action_input):
        action_to_validate = action_input.upper()
        if action_to_validate not in ('ACCEPT', 'TRANSFER', 'OFF', 'STOP'):
            raise ActionUnavailable()
        else:
            return action_to_validate

    @classmethod
    def accept(cls):
        cls.char_list = Equipment.characteristics_builder()
        counter = 0
        if cls.char_list is None:
            pass
        else:
            cls.char_list.append(cls.assigned_to)
            while counter < cls.char_list[6]:
                cls.inv_n = f'eq-{cls.inv}'
                cls.inventory = {cls.inv_n: cls.char_list}
                cls.in_stock.update(cls.inventory)
                counter += 1
                cls.inv += 1
            Warehouse.warehouse_output()

    @classmethod
    def assign_to(cls):
        if not cls.in_stock:
            raise NoEquipmentToTransfer()
            pass
        else:
            what_to_transfer = input('type in the inventory number of equipment and press Enter: ')
            if what_to_transfer not in cls.in_stock.keys():
                raise WrongEqNumber('assign_to')
            else:
                transfer_to = input('type in the department to transfer the equipment to and press Enter: ')
                aux_char = cls.in_stock.get(what_to_transfer)
                update_char = aux_char[:]
                update_char[7] = transfer_to
                update_char_dict = {what_to_transfer: update_char}
                cls.in_stock.update(update_char_dict)
                Warehouse.warehouse_output()

    @classmethod
    def write_off(cls):
        if not cls.in_stock:
            raise NoEquipmentToWriteOff()
            pass
        else:
            write_off = (input('type in the inventory number of equipment to write off and press Enter: '))
            if write_off not in cls.in_stock.keys():
                raise WrongEqNumber('write_off')
            else:
                cls.in_stock.pop(write_off)
                Warehouse.warehouse_output()

    @classmethod
    def warehouse_output(cls):
        print(f"\n{'inv #:':>7}{'equipment type:':>19}{'manufacturer:':>19}{'model:':>15}{'color:':>15}"
              f"{'purchase price:':>19}{'assigned to:':>21}{'comments:':>60}")
        for each in cls.in_stock.items():
            o_inv, o_char = each
            print(f"{o_inv:>7}{o_char[0]:>19}{o_char[1]:>19}{o_char[2]:>15}{o_char[3]:>15}"
                  f"{o_char[4]:>19}{o_char[7]:>21}{o_char[5]:>60}")

    @staticmethod
    def finish_script():
        Warehouse.warehouse_output()
        quit()


class Equipment:

    def __init__(self):
        self.characteristics = []
        self.inventory = []

    @staticmethod
    def characteristics_builder():
        inp_equipment = input("\ntype in the 'type of equipment(printer, scanner, mfd, etc.)', 'manufacturer', "
                              "'model', 'color', 'purchase price', 'amount' \nof the equipment separated by space"
                              " and then press Enter: ")
        inventory = Equipment.characteristics_validator(inp_equipment)
        if not inventory:
            pass
        else:
            type_of_equipment = inventory[0]
            type_of_equipment = type_of_equipment.upper()
            if type_of_equipment == 'PRINTER':
                comments = Printer.char_printer()
            elif type_of_equipment == 'SCANNER':
                comments = Scanner.char_scanner()
            elif type_of_equipment == 'MFD':
                comments = MFD.char_mfd()
            elif type_of_equipment == 'PHONE':
                comments = Phone.char_phone()
            elif type_of_equipment == 'LAPTOP':
                comments = Laptop.char_laptop()
            else:
                comments = input('type in the comments for this type of equipment: ')
            manufacturer = inventory[1]
            model = inventory[2]
            color = inventory[3]
            purchase_price = float(inventory[4])
            amount = int(inventory[5])
            characteristics = [type_of_equipment, manufacturer, model, color, purchase_price, comments, amount]
            return characteristics

    @staticmethod
    def characteristics_validator(data):
        aux_charact = data.split(' ')
        char_to_validate = list(filter(None, aux_charact))
        if len(char_to_validate) != 6:
            raise WrongCharacteristics()
        else:
            price_to_validate = char_to_validate[4]
            amount_to_validate = char_to_validate[5]
            try:
                price_to_validate = float(price_to_validate)
                if price_to_validate <= 0:
                    raise WrongPrice()
            except ValueError:
                print('\033[31mError: price must be a number\033[0m')
                char_to_validate = []
            except WrongPrice as price_err:
                print(price_err)
                char_to_validate = []
            try:
                amount_to_validate = int(amount_to_validate)
                if amount_to_validate <= 0:
                    raise WrongAmount()
            except ValueError:
                print('\033[31mError: amount must be a number\033[0m')
                char_to_validate = []
            except WrongAmount as amount_err:
                print(amount_err)
                char_to_validate = []
            return char_to_validate


class Printer(Equipment):
    equipment_type = 'PRINTER'
    print_dpi = 0
    print_resolution = f'{print_dpi}dpi'
    print_a = 0
    print_format = f'A{print_a}'

    def __init__(self):
        super().__init__()

    @classmethod
    def char_printer(cls):
        cls.print_dpi = input('type in the print resolution(amount of dpi): ')
        cls.print_a = input('type in the print format: A')
        cls.print_resolution = f'{cls.print_dpi}dpi'
        cls.print_format = f'A{cls.print_a}'
        ch_printer = f'{cls.print_resolution}, {cls.print_format}'
        return ch_printer


class Scanner(Equipment):
    equipment_type = 'SCANNER'
    scan_dpi = 0
    scan_resolution = f'{scan_dpi}dpi'
    scan_a = 0
    scan_format = f'A{scan_a}'

    def __init__(self):
        super().__init__()

    @classmethod
    def char_scanner(cls):
        cls.scan_dpi = input('type in the scan resolution(amount of dpi): ')
        cls.scan_a = input('type in the scan format: A')
        cls.scan_format = f'A{cls.scan_a}'
        cls.scan_resolution = f'{cls.scan_dpi}dpi'
        char_printer = f'{cls.scan_resolution}, {cls.scan_format}'
        return char_printer


class MFD(Printer, Scanner):
    equipment_type = 'MFD'
    net_interface = ''

    def __init__(self):
        super().__init__()

    @classmethod
    def char_mfd(cls):
        MFD.char_printer()
        MFD.char_scanner()
        while True:
            has_net_interface = input('does this MFD have net interface (y/n)? ')
            has_net_interface = has_net_interface.upper()
            if has_net_interface == 'Y':
                hni_output = 'has net interface'
                break
            elif has_net_interface == 'N':
                hni_output = 'no net interface'
                break
            else:
                pass
        char_mfd = f'print: {cls.print_resolution}, {cls.print_format}; scan: {cls.scan_resolution}, ' \
                   f'{cls.scan_format}; {hni_output}'
        return char_mfd


class Phone(Equipment):
    equipment_type = 'Phone'

    def __init__(self):
        super().__init__()

    @classmethod
    def char_phone(cls):
        cls.phone_type = input('type in the phone type(smartphone, button phone, etc.): ')
        cls.phone_class = input('type in the phone class(luxury, standard, etc.): ')
        ch_phone = f'{cls.phone_type}, {cls.phone_class}'
        return ch_phone


class Laptop(Equipment):
    equipment_type = 'Laptop'

    def __init__(self):
        super().__init__()

    @classmethod
    def char_laptop(cls):
        cls.laptop_type = input('type in the laptop type(transformer, ultrabook, standard, etc.): ')
        cls.laptop_purpose = input('type in the laptop purpose(design. calculations, etc.): ')
        ch_phone = f'{cls.laptop_type}, {cls.laptop_purpose}'
        return ch_phone


Warehouse.warehouse_management()
