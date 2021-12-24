


from packet import add, show_list, good, help

if __name__ == '__main__':
    # Список учеников
    students = []
    
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала
        command = input(">>> ").lower()
        
        # Выполнить действие в соответствие с командой
        if command == 'exit':
            break
        
        elif command == 'add':
            students.append(add.add())
            
        elif command == 'list':    
            show_list.list(students)
            
        elif command == 'good':
            good.good()
            
        elif command == 'help':
            help.help()
        else:
            print(f"Неизвестная команда {command}")