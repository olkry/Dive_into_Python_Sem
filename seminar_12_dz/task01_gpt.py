import warnings

warnings.filterwarnings('ignore')

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
        subjects_with_data = [subject for subject in self.subjects if
                              self.subjects[subject]['grades'] or self.subjects[subject]['test_scores']]
        subjects_list = ', '.join(subjects_with_data)
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
            for row in reader:
                for subject_name in row:
                    self.subjects[subject_name] = {'grades': [], 'test_scores': []}

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
        average_score = total_score / len(self.subjects[subject]['test_scores']) if self.subjects[subject][
            'test_scores'] else 0
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
