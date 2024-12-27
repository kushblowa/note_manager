# основные данные
username = input('Введите имя пользователя: ')
title_1 = input('Введите заголовок заметки: ')
title_2 = input('Введите подзаголовок (если необходим): ')
title_3 = input('Введите дополнительный заголовок (если необходим): ')
content = input ('Введите содержание заметки: ')
status = input('Укажите статус заметки: ')
created_date = input('Укажите сегодняшнюю дату (ЧЧ.ММ.ГГ): ')
issue_date = input('Укажите дату истечения заметки (ЧЧ.ММ.ГГ): ')
# отображение даты
answer = input("Скрыть год? (Да/Нет): ")
# конечный результат
print("Имя пользователя:", username)
print("Заголовок:", title_1)
if title_2 == '': pass                # на случай, если заголовки после основного не указаны
else: print('Подзаголовок:', title_2)
if title_3 == '': pass
else: print('Дополнительный заголовок:', title_3)
print("Содержание:", content)
print("Статус:", status)
if answer.lower() == 'да':              # отображение даты с/без указания года
    print("Дата создания:", created_date[:5])
    print("Дата истечения:", issue_date[:5])
else:
    if answer.lower() == 'нет':
        print("Дата создания:", created_date)
        print("Дата истечения:", issue_date)
    else:
        print('Неверный тип ответа')

# список для последующего удобства
note = [
username,
title_1,
[title_2, title_3],
content,
status,
created_date,
issue_date
]
print(note)