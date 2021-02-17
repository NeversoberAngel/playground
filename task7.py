"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.

Вместо формы собственности написал форму регистрации бизнеса.
"""

import json

print(f'\nInitial data:')
print(
    f"{'#':<4} {'Company Name':<20} {'Proprietorship':>14} {'TotalRevenue, mln EUR':>24} {'TotalCosts, mln EUR':>24} {'Profit/Loss, mln EUR':>24}")

with open('companies.txt', 'r') as companies:
    companies_list = companies.readlines()
    companies.seek(0)
    all_companies_profit = 0
    companies_with_profit_amount = 0
    companies_dict = {}
    avg_profit_dict = {}
    for each_line in range(len(companies_list)):
        company_line = companies.readline()
        company_data_aux = company_line.split('\n')
        company_data = company_data_aux[0]
        each_company_data = company_data.split('\t')
        each_company_data = [i for i in each_company_data if i != '']
        if each_company_data[-1] == 'TotalCosts,EURmln' and each_company_data[-2] == 'TotalRevenue,EURmln':
            continue
        each_company_data[-1], each_company_data[-2] = float(each_company_data[-1]), float(each_company_data[-2])
        each_company_profit = each_company_data[-2] - each_company_data[-1]
        each_company_profit = round(each_company_profit, 2)

        if each_company_profit > 0:
            all_companies_profit += each_company_profit
            companies_with_profit_amount += 1
        average_profit = all_companies_profit / companies_with_profit_amount
        average_profit = round(average_profit, 2)
        companies_dict.update({each_company_data[1]: each_company_profit})

        row1, row2, row3, row4, row5, row6 = each_company_data[0], each_company_data[1], each_company_data[2], \
                                             each_company_data[3], each_company_data[4], each_company_profit

        print(f"{row1:<4} {row2:<20} {row3:>14} {row4:>24} {row5:>24} {row6:>24}")
    avg_profit_dict.update({'Average profit': average_profit})

    requested_list = []
    requested_list.append(companies_dict)
    requested_list.append(avg_profit_dict)

    print(f'\nRequested dictionary:\n{requested_list}')

with open('final_list.json', 'w') as final_list_json:
    json.dump(requested_list, final_list_json)
