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

# import collections
#
# dd = collections.defaultdict(dict)
# dd['a']['b'] = "foo"
# print(dd)


def thesaurus(user_answer):
    my_list = user_answer.split(', ')
    print(type(my_list))
    idx_list = 0
    while idx_list < len(my_list):
        elem_fam = (my_list[idx_list])
        first_symbol_fam = elem_fam[elem_fam.find(' ') + 1]
        if first_symbol_fam in my_dict:
            my_dict.setdefault(first_symbol_fam).append(elem_fam)
        else:
            my_dict.setdefault(first_symbol_fam, [elem_fam])
        idx_list += 1
    list_of_dict = list(my_dict.values())
    new_list_of_dict = {}
    idx = 0
    print(list_of_dict)
    while len(list_of_dict) != 0:
        new_str = str(list_of_dict.pop(0)).replace("'", '').replace('[', '').replace(']', '')
        my_list_2 = list(new_str.split(', '))
        idx_elem = 0
        # while idx_elem < len(my_list_2):
        #     elem = str(my_list_2[idx_elem])
        #     first_symbol = elem[:1]
        #     if first_symbol in my_dict_name:
        #         my_dict_name.setdefault(first_symbol).append(elem)
        #     else:
        #         my_dict_name.setdefault(first_symbol, [elem])
        #     idx_elem += 1
    # print(my_dict.values())
    # str_val = list(my_dict.values())
    # print(str_val)
    # new_list = str_val.pop(0)
    # print(new_list)
    # print(type(new_list))

            # my_list_elem = elem_fam.split(' ')
            # idx_elem = 0
            # while idx_elem < len(my_list_elem):
            #     elem = str(my_list_elem[idx_elem])
            #     first_symbol = elem[:1]
            #     if first_symbol in my_dict_name:
            #         my_dict_name.setdefault(first_symbol).append(elem)
            #     else:
            #         my_dict_name.setdefault(first_symbol, [elem])
            #     idx_elem += 1


my_dict = {}
my_dict_name = {}
thesaurus('Антон Дутов, Александр Белалов, Евгений Демидов, Анатолий Гончаров, Александр Друзь, '
          'Евгений Дятлов, Кирилл Бондаренко')
# thesaurus_adv(str.title(input('Введите имена через пробел: ')))
print(my_dict)
print(my_dict_name)
