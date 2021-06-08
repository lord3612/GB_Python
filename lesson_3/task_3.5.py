"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
(по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
# >>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]


Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
"""

import random


def get_jokes(n_joke):
    random.shuffle(nouns)
    random.shuffle(adverbs)
    random.shuffle(adjectives)
    if len(nouns) and len(adverbs) and len(adjectives) >= n_joke:
        idx = 0
        while idx < n_joke:
            joke.append([f'{nouns[idx]} {adverbs[idx]} {adjectives[idx]}'])
            idx += 1
    else:
        print(f'Количество слов в словаре меньше, чем необходимо для шуток без повторения')


def get_jokes_rep(n_joke):
    idx = 0
    while idx < n_joke:
        joke.append([f'{nouns[random.randrange(0, len(nouns))]} {adverbs[random.randrange(0, len(adverbs))]} '
                     f'{adjectives[random.randrange(0, len(adjectives))]}'])
        idx += 1


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
joke = []

rep = str(input('Хотите ли вы использовать повтор слов в ваших шутках? y/n: '))
while rep != 'y' and rep != 'n':
    rep = str(input('Введите y/n: '))

if rep == 'y':
    get_jokes_rep(n_joke=int(input(f'Ведите количество шуток от 1 до {len(nouns)}: ')))
elif rep == 'n':
    get_jokes(n_joke=int(input(f'Ведите количество шуток от 1 до {len(nouns)}: ')))
else:
    print('Введите y/n:')

print(joke)


