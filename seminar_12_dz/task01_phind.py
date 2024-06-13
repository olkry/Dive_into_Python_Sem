'''
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. Если ФИО не соответствует условию, выведите:


ФИО должно состоять только из букв и начинаться с заглавной буквы
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:


Предмет {Название предмета} не найден
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). В противном случае выведите:


Оценка должна быть целым числом от 2 до 5

Результат теста должен быть целым числом от 0 до 100
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.


Математика,Физика,История,Литература
Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен иметь следующие методы:
Атрибуты класса:

name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках и результатах тестов для каждого предмета в виде словаря.

Магические методы (Dunder-методы):

__init__(self, name, subjects_file): Конструктор класса. Принимает имя студента и файл с предметами и их результатами. Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.

__setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name. Убеждается, что name начинается с заглавной буквы и состоит только из букв.

__getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.

__str__(self): Возвращает строковое представление студента, включая имя и список предметов.
Студент: Иван Иванов
Предметы: Математика, История

Методы класса:

load_subjects(self, subjects_file): Загружает предметы из файла CSV. Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects.

add_grade(self, subject, grade): Добавляет оценку по заданному предмету. Убеждается, что оценка является целым числом от 2 до 5.

add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету. Убеждается, что результат теста является целым числом от 0 до 100.

get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.

get_average_grade(self): Возвращает средний балл по всем предметам.

Пример

На входе:


student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
На выходе:


Средний балл: 4.5
Средний результат по тестам по математике: 85.0
Студент: Иван Иванов
Предметы: Математика, История

'''

import csv

class NameDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__['name']

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value[0].isupper() or not value.replace(' ', '').isalpha():
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        instance.__dict__['name'] = value

class Student:
    name = NameDescriptor()

    def __init__(self, name: str, subjects_file: str):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        raise AttributeError(f"У объекта Student нет атрибута '{name}'")

    def __str__(self):
        subjects_list = ', '.join(self.subjects.keys())
        return f"Студент: {self.name}\nПредметы: {subjects_list}"

    @staticmethod
    def _validate_grade(grade):
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")

    @staticmethod
    def _validate_test_score(test_score):
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100.")

    def load_subjects(self, subjects_file):
        with open(subjects_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # пропускаем заголовок
            for row in reader:
                subjects_row = []
                for subject_name in row:
                    subjects_row.append(subject_name)
                self.subjects[tuple(subjects_row)] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        self._validate_grade(grade)
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        self._validate_test_score(test_score)
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        total_score = sum(self.subjects[subject]['test_scores'])
        average_score = total_score / len(self.subjects[subject]['test_scores']) if self.subjects[subject]['test_scores'] else 0
        return average_score

    def get_average_grade(self):
        total_grades = []
        for grades in self.subjects.values():
            total_grades.extend(grades['grades'])
        if not total_grades:
            return 0
        return sum(total_grades) / len(total_grades)


# Пример использования
if __name__ == "__main__":
    student = Student("Иван Иванов", "subjects.csv")
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)
    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")
    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")
    print(student)
