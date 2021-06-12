"""
*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
ключевое слово yield.
"""
import itertools


def my_gen(user_answer):
    new_gen = (num for num in range(1, user_answer + 1, 2))
    return new_gen


answer_n = my_gen(int(input('Введите конечное число n генератора: ')))
print(next(answer_n))
print(next(answer_n))
print(next(answer_n))
print(*itertools.islice(answer_n, None))
