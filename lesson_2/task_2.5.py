"""Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться
в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить
рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
(должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по
возрастанию, написав минимум кода?"""

price_list = [57.12, 12.1, 81.73, 91.67, 36.27, 36.53, 1.56, 53.9, 121.66, 44.1, 321.99, 36.1, 142.5, 83.91, 71.12]
my_list = []
for elem in price_list:
    """Ломал голову как выделить дробную часть, точнее как выделить целое число из дробной части, так и не смог!
    При нахождении остатка от деления на 1, после округления, остается либо однозначное (0.1) либо двухзначное (0,12),
    что дальше с этим делать? Как получить целое число 1 и целое 2? Я сначала на 100 умнажил и с 1й копейки 10 получил,
    по итогу только вот через условие допедрил, других выходов не нашел"""
    rub = int(elem)
    right_part = round((elem % 1), 2)
    right_part_str = str(right_part)
    if len(right_part_str) < 4:
        kop = int(right_part * 10)
    else:
        kop = int(right_part * 100)
    my_list.append(f'{rub} руб {kop} коп')
print(my_list)
# Cорт по возрастанию
my_list.sort(key=lambda line: int(line.split(' ')[0]))
print(my_list)
# Сорт по убыванию
my_list_revers = list(reversed(my_list))
print(my_list_revers)
# Самые дорогие по возрастанию
print(list(reversed(my_list_revers[:5])))


