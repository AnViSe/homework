#!/usr/bin/env python

"""
Напишите функцию, которая выводят n-ое число Фибоначчи.
Разрешается использовать временные переменные, циклы и условные операторы.

https://en.wikipedia.org/wiki/Fibonacci_number
"""


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Index must be >= 0")
    result = [0, 1]
    for i in range(2, n + 1):
        result.append(result[-2] + result[-1])
    return result[n]
