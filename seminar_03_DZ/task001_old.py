#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0


def fill_backpack(items, max_weight):
    sorted_items = sorted(items.items(), key=lambda x: (x[1], x[0]), reverse=True)

    backpack = {}
    current_weight = 0

    for item, weight in sorted_items:
        if current_weight + weight <= max_weight and item not in backpack:
            backpack[item] = weight
            current_weight += weight
            max_weight -= weight  # обновление оставшейся грузоподъемности

    return backpack


backpack = fill_backpack(items, max_weight)


backpack = fill_backpack(items, max_weight)