"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
# >>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл
в данном случае использовать функцию re.compile()?
"""
import re

RE_NAME = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9_.+-]+\@[a-zA-Z0-9-]+\.[a-zA-Z]+$')


def email_parse(email_address):
    assert RE_NAME.match(email_address), f'ValueError: wrong email: {email_address}'
    my_dict = {}
    my_dict.update({'username': email_address.split('@')[0]})
    my_dict.update({'domain': email_address.split('@')[1]})
    return my_dict


print(email_parse('ivan.ivanov@mail.ru'))
print(email_parse('123ivan-ivanov@mail.ru'))
print(email_parse('ivan.ivanov@mailru'))
