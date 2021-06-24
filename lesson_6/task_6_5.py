"""
**(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих исходных
файлов и имя выходного файла. Проверить работу скрипта.
"""
import sys
from itertools import zip_longest

open_users, open_hobby, open_users_hobby = sys.argv[1:]
print(f'Взяты исходные файлы "Пользователи" - {open_users}, "Хобби" - {open_hobby} '
      f'и выходной фаил - {open_users_hobby}')
with open(open_users_hobby, 'r+', encoding='utf-8') as users_hobby:
    with open(open_users, encoding='utf-8') as users:
        with open(open_hobby, encoding='utf-8') as hobby:
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
