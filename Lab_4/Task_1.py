import json


def task() -> float:
    """Читает JSON файл и вычисляет сумму произведений score * weight"""
    with open('input.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    total_sum = 0
    for item in data:
        total_sum += item['score'] * item['weight']

    return round(total_sum, 3)


print(task())
