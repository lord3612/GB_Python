"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и пр.
"""


class Matrix:
    def __init__(self, data):
        self.date = data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.date])

    def __add__(self, other):
        result = ''
        if len(self.date) == len(other.date):
            for line_1, line_2 in zip(self.date, other.date):
                if len(line_1) != len(line_2):
                    return 'Ошибка: Разные матрицы'
                my_sum = [x + y for x, y in zip(line_1, line_2)]
                result += ' '.join(map(str, my_sum)) + '\n'
        else:
            return 'Ошибка: Разные матрицы'
        return result


matrix1 = Matrix([[12, 22, 32], [31, 25, 73]])
matrix2 = Matrix([[32, 82, 12], [51, 45, 13], [13, 23, 33]])
matrix3 = Matrix([[12, 32], [25, 73], [23, 33], [11, 22]])
matrix4 = Matrix([[11, 12, 13], [14, 15, 16], [1, 2, 3]])

print(matrix1)
print()
print(matrix2)
print()
print(matrix3)
print()
print(matrix2 + matrix4)