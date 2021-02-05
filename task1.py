# #
# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

a = int(10001011)
b = int(10101000)
c = int(5000)
d = int(1000)
e = str('I am')
f = str('NeverSober Angel')
g = float(3.1415)
h = float(2.718)
i = float(2525.25)
j = float(44.4444)
k = complex(3, 4)
l = complex(7, 8)
m = True
n = False
o = None

x_list = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]
y_list = x_list.copy()

for el in list(y_list):
    print(type(el))
