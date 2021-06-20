import sys

user_num = sys.argv[1:]
num_in_int = [int(item) for item in user_num]
with open('bakery.csv', encoding='utf-8') as show_sale:
    if len(user_num) == 0:
        for line in show_sale:
            print(line.strip())
    elif len(user_num) == 1:
        new_list = list(show_sale.readlines()[num_in_int[0] - 1:])
        for line in new_list:
            print(line.strip())
    elif len(user_num) == 2:
        new_list = list(show_sale.readlines()[num_in_int[0] - 1:num_in_int[1]])
        for line in new_list:
            print(line.strip())
    else:
        print('Ошибка. Аргументы введены не корректно')
