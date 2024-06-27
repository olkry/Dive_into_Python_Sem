'''
Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.
'''

from datetime import datetime

WEEK = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']


def is_leap(year):
    return bool(not year % 4 and year % 100 or not year % 400)


def months(year=2000):
    return (('янв', 31), ('фев', 29 if is_leap(year) else 28), ('мар', 31),
            ('апр', 30), ('мая', 31), ('июн', 30), ('июл', 31), ('авг', 31),
            ('сен', 30), ('окт', 31), ('ноя', 30), ('дек', 31))


# 3-я среда июля
def parse_date(date_txt):
    try:
        week, weekday, month = date_txt.split()
    except:
        raise ValueError

    if not (week[0].isdigit() and 0 < int(week[0]) < 6):
        raise ValueError
    if weekday not in WEEK:
        raise ValueError
    for i, m in enumerate(months(), 1):
        if month[:3] == m[0]:
            return int(week[0]), weekday, i
    raise ValueError


def check_date(text_date):
    week, weekday, month = parse_date(text_date)
    year = datetime.now().year
    first_day_of_month = datetime.strptime(f'01.{month}.{year}', '%d.%m.%Y').weekday()
    current_week = WEEK[first_day_of_month:] + WEEK[:first_day_of_month]
    for i in range(months(year)[month - 1][1]):
        if weekday == current_week[i % 7]:
            week -= 1
            if not week:
                return i + 1
    raise ValueError


text_date = '4-я воскресенье июля'

print(check_date(text_date))
