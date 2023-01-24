# -*- coding: utf-8 -*-
"""
Модуль mastermind_engine реализует функциональность игры.
Содержит функции:
   make_numbers() - компьютер загадывает число по условию что 4 цифры и все разные.
   checking_number() - проверки числа от пользователя на совпадения,
   принимает число от пользователя, возвращает словарь совпадений {'Быки': N, 'Коровы': N}.
"""

from random import randint

make_number = None


def make_numbers():
    # Функция компьютер загадывае число по условию что 4 цифры и все разные
    while True:
        global make_number
        make_number = randint(1000, 9999)
        if len(set(str(make_number))) == 4:
            # Выводится на экран загаданное компьютером число
            print("Загаданное число: ", make_number)
            break


def checking_number(user_number):
    # Функция проверяет число от пользователя на совпадения.
    # Принимает число от пользователя, возвращает словарь совпадений {'Быки': N, 'Коровы': N}.
    bulls = cows = 0
    list_user_number = list(user_number)
    list_make_number = list(str(make_number))
    for i in range(0, 4):
        if list_make_number[i] == list_user_number[i]:
            bulls = bulls + 1
        elif list_make_number[i] in list_user_number:
            cows = cows+1
    return {'Быки': bulls, 'Коровы': cows}
