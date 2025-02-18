import csv
from openpyxl import Workbook

def handler_csv(csv_file, excel_file):
    workbook = Workbook()
    sheet = workbook.active

    with open(csv_file, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        for i, row in enumerate(reader):
            if i == 0:  # for header
                sheet.append(row)
            else:
                updated_row = row.copy()
                if len(updated_row) >= 3:
                    try:
                        # add "руб"
                        updated_row[2] = f"{updated_row[2]} руб"  # 3 row its 'Средний месячный доход'
                        updated_row[3] = f"{updated_row[3]} руб"  # 4 row iss 'Годовой доход'
                    except IndexError: #
                        pass
                sheet.append(updated_row)
    workbook.save(excel_file)
    print("Saved")


handler_csv('companies_fixed.csv', 'companies_fixed.csv')