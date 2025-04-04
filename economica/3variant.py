from tabulate import tabulate

'''
Относительное отклонение
Для первых четырех строк:

Отклонение=
(Отчетный год−Базисный год) / Базисный год ×100

Фондоотдача (руб)

Фондоотдача=
Среднегодовая стоимость основных средств / Стоимость товарной продукции

Фондоотдача активной части (руб)

Фондоотдача активной части=
Среднегодовая стоимость активной части основных средств / Стоимость товарной продукции

Фондоемкость (руб)

Фондоемкость=
Стоимость товарной продукции / Среднегодовая стоимость основных средств


Фондоемкость активной части (руб)

Фондоемкость активной части=
Стоимость товарной продукции / Среднегодовая стоимость активной части основных средств


Рентабельность основных производственных средств (%)

Рентабельность=
Среднегодовая стоимость основных средств/Прибыль от реализации продаж ×100
'''
data = {
    "Показатель": [
        "Стоимость товарной продукции (тыс. руб)",
        "Среднегодовая стоимость основных средств (тыс. руб)",
        "Среднегодовая стоимость активной части основного производства (тыс. руб)",
        "Прибыль от реализации продаж (тыс. руб)",
        "Фондоотдача (руб)",
        "Фондоотдача активной части (руб)",
        "Фондоемкость (руб)",
        "Фондоемкость активной части (руб)",
        "Рентабельность основных производственных средств (%)"
    ],
    "Базисный год": [31679, 148306, 103684, 1467, None, None, None, None, None],
    "Отчетный год": [183553, 148525, 104549, 19892, None, None, None, None, None],
    "Относительное отклонение": [None, None, None, None, None, None, None, None, None]
}

for i in range(4):
    base_value = data["Базисный год"][i]
    report_value = data["Отчетный год"][i]
    relative_deviation = ((report_value - base_value) / base_value) * 100
    data["Относительное отклонение"][i] = round(relative_deviation, 2)

# фондоотдача
base_fund_otdacha = data["Базисный год"][0] / data["Базисный год"][1]
report_fund_otdacha = data["Отчетный год"][0] / data["Отчетный год"][1]
data["Базисный год"][4] = round(base_fund_otdacha, 2)
data["Отчетный год"][4] = round(report_fund_otdacha, 2)
data["Относительное отклонение"][4] = round(
    ((report_fund_otdacha - base_fund_otdacha) / base_fund_otdacha) * 100, 2
)

# фондоотдача актив
base_fund_otdacha_active = data["Базисный год"][0] / data["Базисный год"][2]
report_fund_otdacha_active = data["Отчетный год"][0] / data["Отчетный год"][2]
data["Базисный год"][5] = round(base_fund_otdacha_active, 2)
data["Отчетный год"][5] = round(report_fund_otdacha_active, 2)
data["Относительное отклонение"][5] = round(
    ((report_fund_otdacha_active - base_fund_otdacha_active) / base_fund_otdacha_active) * 100, 2
)

# фондоемкость
base_fund_emkost = data["Базисный год"][1] / data["Базисный год"][0]
report_fund_emkost = data["Отчетный год"][1] / data["Отчетный год"][0]
data["Базисный год"][6] = round(base_fund_emkost, 2)
data["Отчетный год"][6] = round(report_fund_emkost, 2)
data["Относительное отклонение"][6] = round(
    ((report_fund_emkost - base_fund_emkost) / base_fund_emkost) * 100, 2
)

# фондоемкость актив
base_fund_emkost_active = data["Базисный год"][2] / data["Базисный год"][0]
report_fund_emkost_active = data["Отчетный год"][2] / data["Отчетный год"][0]
data["Базисный год"][7] = round(base_fund_emkost_active, 2)
data["Отчетный год"][7] = round(report_fund_emkost_active, 2)
data["Относительное отклонение"][7] = round(
    ((report_fund_emkost_active - base_fund_emkost_active) / base_fund_emkost_active) * 100, 2
)

# рентабельность
base_rent = (data["Базисный год"][3] / data["Базисный год"][1]) * 100
report_rent = (data["Отчетный год"][3] / data["Отчетный год"][1]) * 100
data["Базисный год"][8] = round(base_rent, 2)
data["Отчетный год"][8] = round(report_rent, 2)
data["Относительное отклонение"][8] = round(
    ((report_rent - base_rent) / base_rent) * 100, 2
)

table_data = []
for i in range(len(data["Показатель"])):
    row = [
        data["Показатель"][i],
        data["Базисный год"][i],
        data["Отчетный год"][i],
        data["Относительное отклонение"][i]
    ]
    table_data.append(row)

# Вывод таблицы с использованием tabulate
headers = ["Показатель", "Базисный год", "Отчетный год", "Относительное отклонение"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))