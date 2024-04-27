# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии


def bonus_dict(names: list[str], pays: list[int], bonuses: list[str]):
    worker_dict_bonus = {}
    for name, pay, bonus in zip(names, pays, bonuses):
        # bonus = float(bonus[:-1]) / 100
        worker_dict_bonus[name] = f'{pay * (float(bonus[:-1]) / 100):.0f}'
    return worker_dict_bonus


names_list = ['Степан', 'Владимир', 'Виктория']
pays_list = [56000, 52000, 68000]
bonuses_list = ['10.25%', '14.10%', '8.50%']

print(bonus_dict(names_list, pays_list, bonuses_list))


# ===============================
def salary(name, salar, bonus):
    my_dict = {}
    for i in range(len(name)):
        my_dict[name[i]] = salar[i] * float(bonus[i][:-1]) / 100
    return my_dict


my_name = ["Иван", "Владимир", "Сергей"]
my_salar = [1000, 2000, 3000]
my_bonus = ["10%", "12.2%", "11%"]
print(salary(my_name, my_salar, my_bonus))


# =============================

def dict_salary(name, salary, bonus):
    return {name[i]: salary[i] * float(bonus[i][:-1]) / 100 for i in range(len(name))}


my_name = ["Иван", "Владимир", "Сергей"]
my_salar = [1000, 2000, 3000]
my_bonus = ["10%", "12.2%", "11%"]
print(dict_salary(my_name, my_salar, my_bonus))
