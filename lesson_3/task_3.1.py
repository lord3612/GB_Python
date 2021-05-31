"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
"один"
# >>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.

*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
"""


def num_translate(user_answer):
    for my_key in my_dict:
        if user_answer.istitle() and user_answer == my_key.capitalize():
            cap = str(my_dict.get(my_key))
            print(f'{user_answer} - {cap.capitalize()}')
            return
        elif user_answer == my_key:
            print(f'{user_answer} - {my_dict.get(my_key)}')
            return
    print(f'{user_answer} - {None}')


my_dict = {'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять',
           'zero': 'ноль'}
num_translate(input('Напишите число от 0 до 10 латинскими буквами: '))


