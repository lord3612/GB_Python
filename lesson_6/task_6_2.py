"""
*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
превышает объем ОЗУ компьютера.
"""
from collections import Counter


# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# print(Counter(src))
# result = (Counter(src) for num in src)
# print(list(result))

with open('nginx_logs.txt', encoding='utf-8') as f:
    new_list = []
    for line in f:
        my_gen = ((line[:line.find(' - -')], line[line.find(' "') + 2:line.find(' /')],
                   line[line.find('/d'):line.find(' HTTP')]) for elem in range(1, len(line)))
        new_list.append(next(my_gen))
    spam_list = [f'{num} - спамер, попыток: {num_rep}' for num, num_rep in Counter(new_list).items() if num_rep > 500]
    print(*spam_list, sep='\n')
