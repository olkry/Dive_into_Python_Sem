# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
#
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории
import os
import random
import string


def creat_random_files(quantity: int):
    file_ext = ['txt', 'doc']
    for _ in range(quantity):
        name = ''.join(random.sample(string.ascii_lowercase, 10)) + '.' + random.choice(file_ext)
        with open(f'test_folder/{name}', 'w', encoding='UTF-8') as file:
            file.write(name)


# def creat_random_files(quantity: int):
#     file_ext = ['txt', 'doc']
#     for _ in range(quantity):
#         name = ''.join(random.sample(string.ascii_lowercase, 10)) + '.' + random.choice(file_ext)
#         with open(name, 'w', encoding='UTF-8') as file:
#             file.write(name)


# creat_random_files(10)

def rename_files(desired_name: str = '',
                 num_digits: int = 1,
                 source_ext: str = '',
                 target_ext: str = '___',
                 limits: tuple = (0, 0),
                 path: str = 'test_folder'
                 ):
    counter = 1
    for file in os.listdir('test_folder'):
        if '.' in file:
            name, ext = file.rsplit('.', 1)
        else:
            name, ext = file, ''
        if ext == source_ext or not source_ext:
            re_name = f'{name[limits[0]:limits[1]]}{desired_name if desired_name else ""}{counter:0>{num_digits}}.{target_ext}'
            os.rename(os.path.join('test_folder', file), os.path.join('test_folder', re_name))
            counter += 1


# def rename_files(desired_name: str = '',
#                  num_digits: int = 1,
#                  source_ext: str = '',
#                  target_ext: str = '___',
#                  limits: tuple = (0, 0),
#                  path: str = os.getcwd()
#                  ):
#     counter = 1
#     for file in os.listdir(path):
#         if '.' in file:
#             name, ext = file.rsplit('.', 1)
#         else:
#             name, ext = file, ''
#         if ext == source_ext or not source_ext:
#             re_name = f'{name[limits[0]:limits[1]]}{desired_name if desired_name else ""}{counter:0>{num_digits}}.{target_ext}'
#             os.rename(os.path.join(path, file), os.path.join(path, re_name))
#             counter += 1

# def rename_files(desired_name: str = '',
#                  num_digits: int = 1,
#                  source_ext: str = '',
#                  target_ext: str = '___',
#                  ):
#     counter = 1
#     for file in os.listdir():
#         if '.' in file:
#             name, ext = file.rsplit('.', 1)
#         else:
#             name, ext = file, ''
#         if ext == source_ext or not source_ext:
#             re_name = f'{desired_name if desired_name else ""}{counter:0>{num_digits}}.{target_ext}'
#             os.rename(file, re_name)
#             counter += 1


rename_files(desired_name="file_", num_digits=4, source_ext="txt", target_ext="txt")



# ==============================================
# import os
#
# def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
#     new_names = []
#
#     # Получаем список файлов в текущей директории
#     files = os.listdir('test_folder')
#
#     # Фильтруем только нужные файлы с указанным расширением
#     filtered_files = [file for file in files if file.endswith(source_ext)]
#
#     # Сортируем файлы по имени
#     filtered_files.sort()
#
#     # Задаем начальный номер для порядкового номера
#     num = 1
#
#     # Переименовываем файлы
#     for file in filtered_files:
#         # Получаем имя файла без расширения
#         name = os.path.splitext(file)[0]
#
#         # Если задан диапазон, обрезаем имя файла
#         if name_range:
#             name = name[name_range[0]-1:name_range[1]]
#
#         # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
#         new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext
#
#         # Переименовываем файл
#         path_old = os.path.join(os.getcwd(), folder_name, file)
#         path_new = os.path.join(os.getcwd(), folder_name, new_name)
#         os.rename(path_old, path_new)
#
#         # Увеличиваем порядковый номер
#         num += 1
