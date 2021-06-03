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
        print(f'Курс валюты {currency} на {date.strftime("%d-%m-%Y")} = {course_cur}')
    else:
        print('Такой валюты нет')


if __name__ == '__main__':
    currency_rates(input('Введите код валюты (например, USD, EUR, GBP, ...): '))