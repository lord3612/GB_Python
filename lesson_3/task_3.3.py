"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую
словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся
с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка
по ключам? Можно ли использовать словарь в этом случае?
"""


def thesaurus(user_answer):
    my_list = user_answer.split(' ')
    idx = 0
    while idx < len(my_list):
        elem = str(my_list[idx])
        first_symbol = elem[:1]
        if first_symbol in my_dict:
            my_dict.setdefault(first_symbol).append(elem)
        else:
            my_dict.setdefault(first_symbol, [elem])
        idx += 1


my_dict = {}
thesaurus(str.title(input('Введите имена через пробел: ')))
print(my_dict)

