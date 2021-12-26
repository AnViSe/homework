#!/usr/bin/env python

"""
Напишите функцию, которая проверяет "силу" пароля.

Надёжный пароль:
    - не менее 10 символов
    - содержит буквы разного регистра
    - минимум одну цифру
    - минимум один знак пунктуации
"""
import string


def is_strong_password(pwd: str) -> bool:
    result = False
    len_pwd = len(pwd)
    if len_pwd >= 10:
        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_punct = 0
        for i in range(len_pwd):
            if pwd[i].islower():
                count_lower += 1
                continue
            if pwd[i].isupper():
                count_upper += 1
                continue
            if pwd[i].isdigit():
                count_digit += 1
                continue
            if pwd[i] in string.punctuation:
                count_punct += 1
        result = count_lower > 0 and count_upper > 0 and count_digit > 0 and count_punct > 0 and (
                    count_lower + count_upper + count_digit + count_punct) <= len_pwd
    return result
