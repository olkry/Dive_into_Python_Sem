# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
#
# Пример использования.
# На входе:
# file_path = "C:/Users/User/Documents/example.txt"
#
# На выходе:
# ('C:/Users/User/Documents/', 'example', '.txt')

def get_file_info(file_path: str) -> tuple:
    ender = file_path.rsplit('/', 1)
    path = ender[0] + '/' if len(ender) > 1 else ''
    name, formate = ender[-1].rsplit('.', 1)
    info = (path if len(path) > 0 else '', name, '.'+formate)
    return tuple(info)

file_path = 'file_in_current_directory.txt'

print(get_file_info(file_path))

# =====================================

def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)
