"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей
от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся
в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше
использовать в ответе функции?
"""

from requests import get, utils
from decimal import Decimal
import datetime


def currency_rates(currency):
    date = datetime.datetime.now()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    idx_cur = content.find(currency)
    if idx_cur != -1:
        idx_cur_start = content.index('<Value>', idx_cur)
        idx_cur_end = content.index('</Value>', idx_cur)
        course_cur = Decimal('.'.join(content[idx_cur_start + 7:idx_cur_end].split(',')))
        print(f'Курс валюты {currency} на {date.strftime("%d-%m-%Y %H:%M")} = {course_cur}')
    else:
        print('Такой валюты нет')


currency_rates(input('Введите код валюты (например, USD, EUR, GBP, ...): '))


