"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
1
# >>> next(odd_to_15)
3
...
# >>> next(odd_to_15)
15
# >>> next(odd_to_15)
# ...StopIteration...
"""
import itertools


def my_gen(user_answer):
    for num in range(1, user_answer + 1, 2):
        yield num


answer_n = my_gen(int(input('Введите конечное число n генератора: ')))
# Не понял, как конкретно сделать вывод, нужно в консоли делать? (исходя из примера в задании)?
# В общем вот применение ф-ии next
print(next(answer_n))
print(next(answer_n))
print(next(answer_n))
# Вывод оставшихся
print(*itertools.islice(answer_n, None))



