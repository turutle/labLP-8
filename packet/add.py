def add():
    # Запросить данные об ученике
    name = input("Фамилия и инициалы --> ")
    group = input("Группа --> ")
    rate = list(map(int, input("Оценки --> ")))
            
    # Создать словарь
    student = {
        'name': name,
        'group': group,
        'rate': rate,
    }
            
    # Добавить словарь в список
    return student