# I just converted the companies_fixed.csv file to data.json

import json

def handle_json(old_json, updated_json):

    with open(old_json, 'r', encoding='utf-8') as old:
        data = json.load(old)

    for item in data:
        item['DoThis'] = 'Ускова Вероника Никитична'


    with open(updated_json, 'w', encoding='utf-8') as upd:
        json.dump(data, upd, ensure_ascii=False, indent=4)
        # ensure for correct cyrillic, indent for nice indentation, otherwise the json will remain a single line, unreadable

    print("Saved")


handle_json('data.json', 'updated_data.json')