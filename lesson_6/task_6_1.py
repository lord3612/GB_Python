"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]
"""
with open('nginx_logs.txt', encoding='utf-8') as f:
    new_list = []
    for line in f:
        my_gen = ((line[:line.find(' - -')], line[line.find(' "') + 2:line.find(' /')],
                   line[line.find('/d'):line.find(' HTTP')]) for elem in range(1, len(line)))
        new_list.append(next(my_gen))
    print(*new_list, sep=', \n')


