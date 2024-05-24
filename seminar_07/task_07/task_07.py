# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from ..task_06.task_06 import path_exist, create_file

import os
from pathlib import Path

FILES_TYPE_DICT = {'Video': ['avi', 'mkv', 'mp4'],
                   'Docs': ['doc', 'txt', 'md'],
                   'Music': ['mp3', 'wav'],
                   'Pictures': ['jpg', 'bmp']}


def sort_files(path='test_dir', files_type_dict=FILES_TYPE_DICT):
    file_list = os.listdir(path)
    os.chdir(path)
    for file in file_list:
        extension = file.split('.')[1]
        for key, value in files_type_dict.items():
            if extension in value:
                if not path_exist(key):
                    os.mkdir(key)
    os.replace(file, os.path.join(key, file))


# print(os.listdir('test_dir'))
sort_files()
