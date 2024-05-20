def _leap_year(year: int):
    return bool(not year % 4 and year % 100 or not year % 400)

date_to_prove = '29.2.2020'

day, month, year = date_to_prove.split('.')
day_check = {
    '1': 31,
    '2': 29 if _leap_year(int(year)) else 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31
}

if 0 < int(year) < 10000 and 0 < int(month) < 13 and 0 < int(day) <= day_check[month]:
    print('True')
else:
    print('False')