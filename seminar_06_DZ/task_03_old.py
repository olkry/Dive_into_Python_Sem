# Введите ваше решение ниже

import random


def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга по вертикали, горизонтали или диагонали
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True


def generate_board():
    # Генерируем случайные расстановки ферзей до тех пор, пока не найдем успешную
    while True:
        queens = [(i, random.randint(1, 8)) for i in range(1, 9)]
        if check_queens(queens):
            return queens


def generate_boards():
    # Генерируем 4 успешные расстановки ферзей
    board_list = [generate_board() for _ in range(4)]
    return board_list
