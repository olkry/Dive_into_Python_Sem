# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json

# with (
#     open('task_03.txt', 'r', encoding='utf-8') as f_name,
#     open('s8_task01.json', 'w', encoding='utf-8') as f_json
#     ):
#     text = f_name.readlines()
#     text_dict = {}
#     for item in text:
#         key, value = item.strip().split(' | ')
#         key = key.title()
#         if key in text_dict:
#             text_dict[key].append(value)
#         else:
#             text_dict[key] = [value]
#
#     json.dump(text_dict, f_json, indent=4, ensure_ascii=False)

# =======================================

import json


def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as f:
        text = f.readlines()
        text_dict = {}
        for item in text:
            key, value = item.strip().split(' | ')
        key = key.title()
        if key in text_dict:
            text_dict[key].append(value)
        else:
            text_dict[key] = [value]
        return text_dict


def write_json(file_name, json_data):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    json_data = read_file('names_mult.txt')
    write_json('json.json', json_data)
