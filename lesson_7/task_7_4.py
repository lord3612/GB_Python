"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""
import os

all_files = []
for root, dirs, files in os.walk('../'):
    for file in files:
        all_files.append(os.path.getsize(os.path.join(root, file)))
max_size = max(all_files)

my_dict = {}
i = 1
for x in range(len(str(max_size))):
    i *= 10
    if i == 10:
        my_dict[int(i)] = len([file for file in all_files if i >= file >= 0])
    else:
        my_dict[int(i)] = len([file for file in all_files if i >= file >= i / 10])
print(my_dict)