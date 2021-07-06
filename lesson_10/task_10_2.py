"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""
from abc import ABC, abstractmethod


class MyAbsClass(ABC):
    @abstractmethod
    def __init__(self, parameter_v, parameter_h):
        pass

    @abstractmethod
    def costume(self):
        pass

    @abstractmethod
    def coat(self):
        pass


class Clothes(MyAbsClass):
    def __init__(self, parameter_v, parameter_h):
        self.parameter_v = parameter_v
        self.parameter_h = parameter_h

    @property
    def costume(self):
        return self.parameter_h * 2 + 0.5

    @property
    def coat(self):
        return self.parameter_v / 6.5 + 0.5


clothes = Clothes(10, 20)
print(clothes.costume)
print(clothes.coat)