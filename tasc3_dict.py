# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Через словарь

year = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8:'8', 9:'9', 10:'10', 11:'11', 12:'12'}
print(year)

month = input('Введите месяц в виде числа от 1 до 12: ')
if month == year.get(3) or month == year.get(4) or month == year.get(5):
    print('этот месяц  весной')
elif month == year.get(6) or month == year.get(7) or month == year.get(8):
    print('этот месяц летом')
elif month == year.get(9) or month == year.get(10) or month == year.get(11):
    print('этот месяц осенью')
elif month == year.get(12) or month == year.get(1) or month == year.get(2):
    print('этот месяц зимой')
else:
    print('не знаю, в каком сезоне этот месяц')

