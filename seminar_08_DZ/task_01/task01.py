'''
Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию и все вложенные директории.
Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:
Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или директория.
Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах. Важные детали:
Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
Для файлов сохраните их размер в байтах.
Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории, и вложенных директорий.
Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
Для обхода файловой системы вы можете использовать модуль os.
Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и
возвращать результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных
файлах (JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном обходе директорий.
При этом сначала добавляются файлы, а затем директории.
Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)),
и затем получается размер файла (size = os.path.getsize(path)). Информация о файле добавляется в список results
в виде словаря {'Path': path, 'Type': 'File', 'Size': size}.
Затем, для каждой директории (name в dirs), также создается полный путь к директории (path = os.path.join(root, name)),
и вызывается функция get_dir_size(path), чтобы получить размер всей директории с учетом ее содержимого.
Информация о директории добавляется в список results в виде словаря {'Path': path, 'Type': 'Directory', 'Size': size}.
'''

import os
import sys
import json
import csv
import pickle


# def size_of_dir(dir_path: str) -> int:
#     total_size = 0
#     for path, _, files in os.walk(dir_path):
#         for file in files:
#             total_size += sys.getsizeof(os.path.join(path, file))
#     return total_size
#
#
# def save_results_to_json(cur_path: str, sours: dict[str, dict]):
#     name = os.path.join(cur_path, 'result.json')
#     with open(name, 'w', encoding='UTF-8') as data:
#         json.dump(sours, data, indent=4, ensure_ascii=False)
#
#
# def save_results_to_csv(cur_path: str, sours: dict[str, dict]):
#     name = os.path.join(cur_path, 'result.csv')
#     file = [['Full_path', 'name', 'parent_dir', 'type', 'size']]
#     for key, item in sours.items():
#         file.append([key, *item.values()])
#     with open(name, 'w', encoding='utf-8') as data:
#         write_csv = csv.writer(data, dialect='excel', delimiter=',')
#         write_csv.writerows(file)
#
#
# def save_results_to_pickle(cur_path: str, sours: dict[str, dict]):
#     name = os.path.join(cur_path, 'result.bin')
#     with open(name, 'wb') as data:
#         pickle.dump(sours, data)
#
#
# def traverse_directory(full_path: str = os.getcwd()):
#     result = {}
#     for path, dir_list, file_list in os.walk(full_path):
#         for cur_dir in dir_list:
#             result[os.path.join(path, cur_dir)] = {'name': cur_dir, 'path': path, 'type': 'DIR',
#                                                    'size': size_of_dir(os.path.join(path, cur_dir))}
#         for cur_file in file_list:
#             result[os.path.join(path, cur_file)] = {'name': cur_file, 'path': path, 'type': 'FILE',
#                                                     'size': sys.getsizeof(os.path.join(path, cur_file))}
#
#     save_results_to_json(full_path, result)
#     save_results_to_pickle(full_path, result)
#     save_results_to_csv(full_path, result)
#
#     return result
#
#
# print(traverse_directory('G:\GeekBrains\\002_Dive_into_Python_Sem'))

# =====================

import os
import json
import csv
import pickle


def get_dir_size(directory):
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            total_size += os.path.getsize(path)

    return total_size


def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})

        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})

    return results


def save_results_to_json(results, file_path):
    with open(file_path, 'w') as file:
        json.dump(results, file)


def save_results_to_csv(results, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(results)


def save_results_to_pickle(results, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(results, file)


traverse_directory('G:\GeekBrains\\002_Dive_into_Python_Sem')