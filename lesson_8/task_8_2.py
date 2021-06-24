"""
*(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
для получения информации вида:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000]
"GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
Можно ли для них уточнить регулярное выражение?
"""
import re
REMOTE_ADDR = re.compile(r'\d+\.\d+\.\d+\.\d+')
REQUEST_DATETIME = re.compile(r'\d+/\w+/\d+:\d+:\d+:\d+\s[+]\d+')
REQUEST_TYPE = re.compile(r'[A-Z]{3}')
REQUESTED_RESOURSE = re.compile(r'[/][a-z]+[/][a-z]+[_][0-9]+')
RESPONSE_CODE_SIZE = re.compile(r'\s\d{1,3}')
# Хватило ума только на то, что бы объединить CODE и SIZE

with open('nginx_logs.txt', encoding='utf-8') as log_file:
    for line in log_file.readlines():
        parsed_raw = (re.search(REMOTE_ADDR, line).group(0), re.search(REQUEST_DATETIME, line).group(0),
                      re.search(REQUEST_TYPE, line).group(0), re.search(REQUESTED_RESOURSE, line).group(0),
                      tuple(re.findall(RESPONSE_CODE_SIZE, line)))
        print(parsed_raw)
