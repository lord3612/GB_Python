"""
*(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные данные
в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: горные лыжи
"""
from itertools import zip_longest
with open('users_hobby.txt', 'r+', encoding='utf-8') as users_hobby:
    with open('users.csv', encoding='utf-8') as users:
        with open('hobby.csv', encoding='utf-8') as hobby:
            # Проверка количества строк в файлах
            if sum(1 for line_user in users) < sum(1 for line_hobby in hobby):
                exit(1)
            # Возврат к началу документа
            users.seek(0)
            hobby.seek(0)
            # Решение задичи
            for line_user, line_hobby in zip_longest(users, hobby):
                users_hobby.write(f'{line_user.strip()}: '
                                  f'{line_hobby.strip() if line_hobby is not None else line_hobby}\n')
            users_hobby.seek(0)
            print(users_hobby.read())

