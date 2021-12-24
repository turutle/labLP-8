def list(students):
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 11
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^11} |'.format(
            "№",
            "Ф.И.О.",
            "Группа",
            "Оценки"
        )
    )
    print(line)

    # Вывести данные о всех учениках
    for idx, student in enumerate(students, 1):
        print(
            '| {:<4} | {:<30} | {:<20} |'.format(
                idx,
                student.get('name', ''),
                student.get('group', '')
            ), end=' ')
        for i in student.get('rate'):
            print(i, end=' ')
        print('|')
    print(line)