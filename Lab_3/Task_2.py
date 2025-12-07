def find_common_participants(group1, group2, separator=","):
    """Возвращает список общих участников двух групп"""
    # Разбиваем строки на списки и удаляем пробелы
    participants1 = set(name.strip() for name in group1.split(separator))
    participants2 = set(name.strip() for name in group2.split(separator))

    common = participants1 & participants2

    return sorted(list(common))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяем работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(f"Общие участники: {common_participants}")