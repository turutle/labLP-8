def good():
    # Инициализировать счетчик
    count = i = 0
            
    for student in students:
        marks = student.get('rate')
        while i < len(marks):
            if marks[i] < 4:
                break
            if i+1 == len(marks):
                count += 1
                print('{:>4}: {}'.format(count, student.get('name', '')))
            i += 1    
                
    # Если счетчик равен 0, то хорошие ученики не найдены
    if count == 0:
        print("Ученики с хорошими и отличными оценками не найдены")