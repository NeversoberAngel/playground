# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Через list
# Добавление списска месяцев
ref = []
m = 1
while m <= 13:
    ref.append(m)
    m += 1
ref.pop(-1)
# print(ref)

month = int(input('Введите месяц в виде числа от 1 до 12: '))
if month == ref[2] or month == ref[3] or month == ref[4]:
    print('этот месяц весной')
elif month == ref[5] or month == ref[6] or month == ref[7]:
    print('этот месяц летом')
elif month == ref[8] or month == ref[9] or month == ref[10]:
    print('этот месяц осенью')
elif month == ref[11] or month == ref[0] or month == ref[1]:
    print('этот месяц зимой')
else:
    print('не знаю, в каком сезоне этот месяц')
