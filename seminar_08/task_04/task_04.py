'''Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.'''

import csv
import json

from seminar_08.task_01.task01 import write_json



def read_csv(file_name):
    csv_data = []
    with open(file_name, 'r', newline='', encoding='utf-8') as f:
        for line in csv.reader(f, dialect='excel-tab'):
            csv_data.append(line)
    return csv_data


def convert_csv_data(csv_data):
    for item in csv_data:
        item[1] = item[1].zfill(10)
        item.append(hash(item[1] + item[2]))
    return {item[-1]: item[:-1] for item in csv_data}


if __name__ == '__main__':
    csv_data = read_csv('../task_03/csv_users.csv')
    write_json('s8_t04.json', convert_csv_data(csv_data))
