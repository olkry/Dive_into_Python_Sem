'''
Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
'''

import json


class User:
    def __init__(self, user_id, name, level):
        self.id = user_id
        self.name = name
        self.level = level

    def __repr__(self):
        return f'{self.name} ({self.id}, {self.level})'


class Company:
    def __init__(self):
        self.user_list = []
        self.path = "G:/GeekBrains/002_Dive_into_Python_Sem/seminar_08/task_02/users.json"
        self.reading_file_json()

    def reading_file_json(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            json_data = dict(json.load(file))
            for level, user in json_data.items():
                for user_id, user_name in dict(user).items():
                    self.user_list.append(User(user_id, user_name, level))



if __name__ == '__main__':
    compamy = Company()
    print(compamy.user_list)
