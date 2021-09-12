#!/usr/bin/env python

"""
Напишите функцию, которая проверяет, является ли целое положительное число палиндромом.

Можно работать только с числами, конвертировать в строку нельзя :)
"""
import math


def is_palindrom(n: int) -> bool:
    if n <= 0:
        raise ValueError("Number must be a positive integer")

    while n > 9:
        power = 10 ** math.floor(math.log10(n))
        # Сравниваем первую и последнюю цифру
        if n // power != n % 10:
            break
        # Обрезаем первую и последнюю цифру
        n = (n - (n // power) * power) // 10
    else:
        return True
    return False
