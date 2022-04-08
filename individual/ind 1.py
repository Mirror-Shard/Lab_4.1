#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first - целое число, левая граница диапазона, включается в диапазон; поле
second — целое число, правая граница диапазона, не включается в диапазон. Пара
чисел представляет полуоткрытый интервал (first, second). Реализовать метод
rangecheck() — проверку заданного целого числа на принадлежность диапазону.
"""


class Interval:

    def __init__(self):
        self.first = 0
        self.second = 0
        self.span = []

    def read(self, first=0, second=0):
        if first or second:
            self.first = first
            self.second = second
            self.span = make_span(self.first, self.second)
        else:
            print("Числа не были переданы")

    def display(self):
        print(self.span)

    def range_check(self, num):
        # Проверка существования интервала
        if self.span:
            if num in self.span:
                print("Число присутствует в интервале")
            else:
                print("Число отсутствует в интервале")
        else:
            print("Интервала не существует")


def make_span(first, second):
    if first < second:
        span = [i for i in range(first, second)]
    else:
        span = [i for i in range(first, second, -1)]
    return span


if __name__ == '__main__':

    interval = Interval()

    while True:

        first = int(input("\nВведите левую границу интервала: "))
        second = int(input("Введите правую границу интервала: "))
        interval.read(first, second)
        interval.display()
        # Проверка нахождения числа в интервале
        num = int(input("Введите число: "))
        interval.range_check(num)
