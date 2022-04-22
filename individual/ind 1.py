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

    def read(self, first=0, second=0):
        if first or second:
            self.first = first
            self.second = second
        else:
            print("Числа не были переданы")

    def display(self):
        print(f"Интервал начинается с {self.first} и до {self.second}")

    def range_check(self, num):
        return first <= num <= second


if __name__ == '__main__':

    interval = Interval()

    while True:

        first = int(input("\nВведите левую границу интервала: "))
        second = int(input("Введите правую границу интервала: "))
        interval.read(first, second)
        interval.display()
        # Проверка нахождения числа в интервале
        num = int(input("Введите число: "))
        if interval.range_check(num):
            print("Число присутствует в интервале")
        else:
            print("Число отсутствует в интервале")
