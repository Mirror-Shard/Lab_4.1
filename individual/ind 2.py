#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создать класс Time для работы со временем в формате «час:минута:секунда».
Класс должен включать в себя не менее четырех функций инициализации: числами,
строкой (например, «23:59:59»), секундами и временем. Обязательными операциями
являются: вычисление разницы между двумя моментами времени в секундах,
сложение времени и заданного количества секунд, вычитание из времени заданного
количества секунд, сравнение моментов времени, перевод в секунды,
перевод в минуты (с округлением до целой минуты).
"""
from inspect import isclass


class Time:

    def __init__(self, s, m=0, h=0):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        # Если передана строка "23:59:59"
        if type(s) == str:
            hours = "0"
            minutes = "0"
            seconds = "0"
            # Изъятие из строки в переменную: Часы
            for i, item in enumerate(s):
                if item.isdigit():
                    hours += item
                else:
                    s = s[i + 1:]
                    break
            # Минуты
            for i, item in enumerate(s):
                if item.isdigit():
                    minutes += item
                else:
                    s = s[i + 1:]
                    break
            # Секунды
            for i, item in enumerate(s):
                if item.isdigit():
                    seconds += item
                else:
                    break
            self.hours = int(hours)
            self.minutes = int(minutes)
            self.seconds = int(seconds)
            self.__update()

        # Если передано время(классом Time)
        elif isclass(s):
            self.hours = s.hours
            self.minutes = s.minutes
            self.seconds = s.seconds

        # Если передана одна переменная секунды 86400
        elif s and m == 0 and 0 == h:
            self.seconds = s
            self.__update()

        # Если переданы числа 23 59 59
        elif s and m or h:
            self.hours = h
            self.minutes = m
            self.seconds = s
            self.__update()

        else:
            print("Ошибка")

    # Обновление и упорядочивание значений класса
    def __update(self):
        # Переводит отрицательные в положительные
        while self.seconds < 0:
            self.minutes -= 1
            self.seconds += 60
        while self.minutes < 0:
            self.hours -= 1
            self.minutes += 60
        while self.hours < 0:
            self.hours += 24
        # Сортировка hours, minutes, seconds по 23:59:59
        while self.seconds >= 60:
            self.minutes += 1
            self.seconds -= 60
        while self.minutes >= 60:
            self.hours += 1
            self.minutes -= 60
        while self.hours >= 24:
            self.hours -= 24

    # Разность в секундах
    def difference(self, seconds):
        if not seconds:
            seconds = int(input("Введите количество вычитаемых секунд: "))
        self.seconds -= seconds
        self.__update()

    # Сумма в секундах
    def sum(self, seconds):
        if not seconds:
            seconds = int(input("Введите количество прибавляемых секунд: "))
        self.seconds += seconds
        self.__update()

    # Вычисление разницы между моментами времени
    def distinction(self, time):
        dist = self
        dist.seconds -= time.seconds
        dist.minutes -= time.minutes
        dist.hours -= time.hours
        dist.__update()
        return dist.display()

    def display(self):
        print(f"{self.hours}:{self.minutes}:{self.seconds}")


if __name__ == '__main__':

    print("### Создание первого Time секундами ###")
    a = Time(3600)
    a.display()

    print("\n### Создание второго Time строкой ###")
    b = Time("1:6:40")
    b.display()

    print("\n### Сумма a+3600 ###")
    a.sum(3600)
    a.display()

    print("\n### Разность b-3600 ###")
    b.difference(3600)
    b.display()

    print("\n### Разница a b ###")
    a.distinction(b)
