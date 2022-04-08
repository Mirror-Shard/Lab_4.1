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


class Time:

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.time = "hours:minutes:seconds"
        self.all_seconds = 0

    # Задать время секундами 86400
    def read_seconds(self, seconds=0):
        if not seconds:
            seconds = int(input("Введите количество секунд: "))
        self.__update(seconds)

    # Задать время числами
    def read_numbers(self, hours, minutes, seconds):
        if not hours or minutes or seconds:
            hours = int(input("Введите количество часов: "))
            minutes = int(input("Введите количество минут: "))
            seconds = int(input("Введите количество секунд: "))
        self.__update(seconds, minutes, hours)

    # Задать время другим временем(классом Time)
    def read_time(self, time):
        self.__update(time.all_seconds)

    # Задать время строкой "23:59:59"
    def read_string(self, string=0):
        if not string:
            string = input("Введите время в формате \"часы:минуты:секунды\" : ")
        hours = "0"
        minutes = "0"
        seconds = "0"
        # Изъятие из строки в переменную: Часы
        for i, item in enumerate(string):
            if item.isdigit():
                hours += item
            else:
                string = string[i+1:]
                break
        # Минуты
        for i, item in enumerate(string):
            if item.isdigit():
                minutes += item
            else:
                string = string[i+1:]
                break
        # Секунды
        for i, item in enumerate(string):
            if item.isdigit():
                seconds += item
            else:
                break
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
        self.__update(seconds, minutes, hours)

    # Обновление значений класса
    def __update(self, seconds, minutes=0, hours=0):
        # Если передано отрицательное время
        if seconds < 0:
            seconds = 86400 - abs(seconds)
        # Сортировка hours, minutes, seconds по 23:59:59
        while seconds >= 60:
            minutes += 1
            seconds -= 60
        while minutes >= 60:
            hours += 1
            minutes -= 60
        while hours >= 24:
            hours -= 1
        #
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.time = f"{hours}:{minutes}:{seconds}"
        self.all_seconds = hours*3600 + minutes*60 + seconds

    # Разность в секундах
    def difference(self, seconds):
        if not seconds:
            seconds = int(input("Введите количество вычитаемых секунд: "))
        self.all_seconds -= seconds
        self.__update(self.all_seconds)

    # Сумма в секундах
    def sum(self, seconds):
        if not seconds:
            seconds = int(input("Введите количество прибавляемых секунд: "))
        self.all_seconds += seconds
        self.__update(self.all_seconds)

    # Вычисление разницы между моментами времени
    def distinction(self, time):
        s_sec = self.all_seconds
        t_sec = time.all_seconds
        dist = s_sec - t_sec
        if dist > 0:
            print(f"Больше на {dist} секунд")
        elif dist < 0:
            print(f"Меньше на {dist} секунд")
        else:
            print("Разницы нет, оба времени одинаковы")

    def display(self):
        # print(f"Часы - {self.hours}")
        # print(f"Минуты - {self.minutes}")
        # print(f"Секунды - {self.seconds}")
        print(f"Время - {self.time}")
        print(f"Все секунды - {self.all_seconds}")


if __name__ == '__main__':

    print("### Создание первого Time ###")
    a = Time()
    a.read_seconds(3600)
    a.display()

    print("\n### Создание второго Time ###")
    b = Time()
    b.read_string("1:6:40")
    b.display()

    print("\n### Сумма a+b ###")
    a.sum(b.all_seconds)
    a.display()

    print("\n### Разность b-a ###")
    b.difference(a.all_seconds)
    b.display()

    print("\n### Разница a b ###")
    a.distinction(b)

