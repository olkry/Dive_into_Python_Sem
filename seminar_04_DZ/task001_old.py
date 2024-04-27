#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# matrix = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# transposed_matrix = transpose(matrix)

# Введите ваше решение ниже

def transpose(matrix):
    transposed_matrix = [list(row) for row in zip(*matrix)]
    return transposed_matrix

# transposed_matrix = transpose(matrix)
# print(transposed_matrix)