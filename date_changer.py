created_date = '18-12-2024'
issue_date = '25-12-2024'
answer = input("Скрыть год? (Да/Нет): ")
if answer.lower() == 'да':
    print(created_date[0:5])
    print(issue_date[0:5])
else:
    if answer.lower() == 'нет':
        print(created_date)
        print(issue_date)
    else:
        print('Неверный тип ответа')



