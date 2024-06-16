'''
Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение доступа.
А если пользователь есть, получите его уровень из множества пользователей.
добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
'''

import json

from task03 import *





class User:
    def __init__(self, user_id, name, level):
        self.id = user_id
        self.name = name
        self.level = level

    def __repr__(self):
        return f'{self.name} ({self.id}, {self.level})'

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id

    def __hash__(self):
        return hash(f'{self.id}')


class Company:
    def __init__(self):
        self.user_set = set()
        self.path = "G:/GeekBrains/002_Dive_into_Python_Sem/seminar_08/task_02/users.json"
        self.reading_file_json()

    def reading_file_json(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            json_data = dict(json.load(file))
            for level, user in json_data.items():
                for user_id, user_name in dict(user).items():
                    self.user_set.add(User(user_id, user_name, level))

    def login(self, user_id, user_name):
        log_user = User(user_id, user_name, 0)
        for user in self.user_set:
            if user == log_user:
                print('Authorization complete!')
                self.authorization_user = user
                return user.level
        raise AccessError

    def add_user(self, user_id, user_name, level):
        if int(self.authorization_user.level) > level:
            raise LevelError
        new_user = User(user_id, user_name, level)
        print(f'Пользователь {user_name} добавлен')
        self.user_set.add(new_user)


if __name__ == '__main__':
    company = Company()
    company.login('17', 'Сергей')
    print(company.authorization_user)
    company.add_user('42', 'Олег', 1)
    print(company.user_set)

