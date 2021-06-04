"""
*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:

# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}

Как поступить, если потребуется сортировка по ключам?

"""

import collections


def thesaurus(user_answer):  # 2 дня код писал, по итогу не вышло того что хотел, сдаюсь!
    my_list = user_answer.split(', ')  # часть кода таже, что и в задаче 3.3
    idx_list = 0
    while idx_list < len(my_list):
        elem_fam = (my_list[idx_list])
        first_symbol_fam = elem_fam[elem_fam.find(' ') + 1]
        if first_symbol_fam in my_dict_fam:
            my_dict_fam.setdefault(first_symbol_fam).append(elem_fam)
        else:
            my_dict_fam.setdefault(first_symbol_fam, [elem_fam])
        idx_list += 1  # тут заканчивается самая адекветная часть кода, где все хорошо работает
    list_of_dict = list(my_dict_fam.values())  # что бы как то работать с конечными значениями словаря я решил их
    list_key = list(my_dict_fam.keys())  # выделить в отдельный лист
    while len(list_of_dict) != 0:  # потом понял что в листе оказались лишние лимволы
        new_str = str(list_of_dict.pop(0)).replace("'", '').replace('[', '').replace(']', '')
        my_list_2 = list(new_str.split(', '))  # тут я решил что можно в принципе сделать что-то похожее из 1й части
        idx_elem = 0
        while idx_elem < len(my_list_2):
            elem = str(my_list_2[idx_elem])
            first_symbol = elem[:1] # из практики понял, что метод из 1й части кода не подходит
            # if first_symbol in my_dict_name:
            # my_dict_name.setdefault(first_symbol).append(elem)
            my_dict = collections.defaultdict(dict)  # и ура, нашел вроде бы, как мне показалось подходящий метод
            my_dict[list_key[idx_elem]][first_symbol] = elem  # решиния, но шиш! Дальше пытаться уже не стал, сдался!
            print(my_dict)  # результат решения до которого я дошел! По-моему я куда-то не туда ушел.
            #     my_dict_name.setdefault(first_symbol).append(elem)
            # else:
            #     my_dict_name.setdefault(first_symbol, [elem])
            #     my_dict[list_key[idx_elem]][first_symbol] = elem
            idx_elem += 1


my_dict_name = {}
my_dict_fam = {}
thesaurus('Иван Сергеев, Инна Серова, Петр Алексеев, Илья Иванов, Анна Савельева')
print(my_dict_fam)




