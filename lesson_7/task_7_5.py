"""
*(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }

Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""
import os
import json

all_files = []
for root, dirs, files in os.walk('./'):
    for file in files:
        all_files.append((os.path.join(root, file).split('.')[-1], os.path.getsize(os.path.join(root, file))))
max_size = max(all_files, key=lambda x: x[1])[1]

my_dict = {}
i = 1
for x in range(len(str(max_size))):
    i *= 10
    if i == 10:
        my_dict[int(i)] = len([file for extension, file in all_files if i >= file >= 0]), \
                          list(set([extension for extension, file in all_files if i >= file >= 0]))
    else:
        my_dict[int(i)] = len([file for extension, file in all_files if i >= file >= i / 10]), \
                          list(set([extension for extension, file in all_files if i >= file >= i / 10]))

print(my_dict)
with open(os.path.basename(os.getcwd()) + '_summary.json', 'w') as file_json:
    json.dump(my_dict, file_json)
