# Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
# задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
print('Задание 1.3')
user_answer = int(input('Введите число до 20: '))
# Отрицательное число - подходит любое)))
answer = list(str(int(user_answer)))
if user_answer < 0:
    answer.remove('-')
last_elem1 = int(answer[-1])
if user_answer <= 20:
    if len(answer) > 1:
        last_elem2 = int(answer[-2])
        if last_elem2 == 1 or last_elem1 == 0 or last_elem1 >= 5:
            print(f'Получаем {user_answer} процентов')
        elif last_elem1 == 1:
            print(f'Получаем {user_answer} процент')
        elif 1 < last_elem1 < 5:
            print(f'Получаем {user_answer} процента')
    elif last_elem1 == 0 or last_elem1 >= 5:
        print(f'Получаем {user_answer} процентов')
    elif last_elem1 == 1:
        print(f'Получаем {user_answer} процент')
    elif 1 < last_elem1 < 5:
        print(f'Получаем {user_answer} процента')
else:
    print('Введите число до 20!')

