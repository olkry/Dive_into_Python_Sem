# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

def company_verification(company: dict):
    profit = []
    for comp in company:
        profit.append(sum(company[comp]))
    return all(map(lambda x: x > 0, profit))


# business = {'Карнавал': [824, 555, 283], 'Парсек': [662, 883, 441, 663], 'Манго': [89, 23, 95, 12]}  #True
business = {'Карнавал': [824, 555, 283], 'Парсек': [662, 883, 441, 663], 'Манго': [89, 23, 95, 12, -999]}  # False
companies = {
    'Abibas': [1234, -456, 2345, 1000, 800],
    'Nuke': [-3000, 5600, -8000],
    'Ribok': [5000, -2300, -4000, 9000]
}
print(company_verification(companies))


# ==================================


def is_profit(dct_companies: dict) -> bool:
    for profit in dct_companies.values():
        if sum(profit) < 0:
            return False
    return True


dct_companies = {
    'Abibas': [1234, -456, 2345, 1000, 800],
    'Nuke': [-3000, 5600, 8000],
    'Ribok': [5000, -2300, -4000, 9000]
}

print(is_profit(dct_companies))


# ============================

def is_profit(dct_companies: dict) -> bool:
    return all([sum(val) > 0 for val in dct_companies.values()])


dct_companies = {
    'Abibas': [1234, -456, 2345, 1000, 800],
    'Nuke': [-3000, 5600, 8000],
    'Ribok': [5000, -2300, -4000, 9000]
}

print(is_profit(dct_companies))


# ============================


def is_profit(dct_companies: dict) -> bool:
    return all(map(lambda x: sum(x) > 0, dct_companies.values()))


dct_companies = {
    'Abibas': [1234, -456, 2345, 1000, 800],
    'Nuke': [-3000, 5000, 8000],
    'Ribok': [5000, -2300, -4000, 9000]
}

print(is_profit(dct_companies))
