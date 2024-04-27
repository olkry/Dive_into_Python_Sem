# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


def sum_on_range(numbers: list[int], start: int, end: int):
    # start, end = min(start, end), max(start, end)
    start, end = sorted([start, end])
    if end > len(numbers):
        end = len(numbers) - 1
    if start < 0:
        start = 0
    # return sum(numbers[num] for num in range(start, end + 1))
    return sum(numbers[start:end + 1])


nums = [16, 843, 514, 345, 4734354, 43, 6, 5, 4, 9, 4, 313, 454, 34]
starting, finish = 8, 5
print(sum_on_range(nums, starting, finish))

# ==========================


def sum_slice(int_list: list[int], a_index: int, b_index: int) -> int:
    a_index, b_index = sorted([a_index, b_index])
    if a_index < 0:
        a_index = 0
    if b_index < 0:
        b_index = 1
    return sum(int_list[a_index:b_index + 1])


print(sum_slice([1, 2, 3, 4, 5, 6], -1, 2))