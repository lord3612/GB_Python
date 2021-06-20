"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби. Известно, что при хранении
данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код,
загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби  (hobby.csv):
скалолазание,охота
горные лыжи
"""
# Создал и заполнил файлы
# users = open('users.csv', 'w', encoding='utf-8')
# users.write('Иванов,Иван,Иванович\nПетров,Петр,Петрович')
# users.close()
#
# hobby = open('hobby.csv', 'w', encoding='utf-8')
# hobby.write('скалолазание,охота\nгорные лыжи')
# hobby.close()
import json
from itertools import zip_longest

with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        # Проверка количества строк в файлах
        if sum(1 for line_user in users) < sum(1 for line_hobby in hobby):
            exit(1)
        # Возврат к началу документа
        users.seek(0)
        hobby.seek(0)
        # Решение задичи
        my_dict = {}
        for line_user, line_hobby in zip_longest(users, hobby):
            my_dict[line_user.strip()] = line_hobby.strip() if line_hobby is not None else line_hobby

with open('users_hobby.json', 'r+', encoding='utf-8') as users_hobby:
    json.dump(my_dict, users_hobby, ensure_ascii=False)
    data = json.load(users_hobby)
    print(data)
