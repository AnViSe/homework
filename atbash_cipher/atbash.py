#!/usr/bin/env python

"""
Напишите программу, которая кодирует и декодирует текст шифром Атбаш.
В этом шифре каждая i-ая буква алфавита заменяется i-ой буквой с его конца, например, для латинского алфавита: a - z, b - y и т.д.

- заглавные буквы переводятся в строчные
- пробельные символы и знаки препинания опускаются
- шифр идёт блоками по 5 символов, между ними пробел

Пример:

`Bambarbia, Kirgudu` -> `yznyz iyrzp ritfw f`
"""
import string

BLOCK_SIZE = 5


def revert_char(alpha: str) -> str:
    if alpha.isalpha():
        position = string.ascii_lowercase.index(alpha.lower()) + 1
        return string.ascii_lowercase[-position]
    elif alpha in string.punctuation or alpha in string.whitespace:
        return
    else:
        return alpha


def atbash_encode(text: str) -> str:
    result = ''.join(revert_char(c) for c in text if revert_char(c))
    result = ' '.join(result[i:i + BLOCK_SIZE] for i in range(0, len(result), BLOCK_SIZE))
    return result


def atbash_decode(cipher: str) -> str:
    return ''.join(revert_char(c) for c in cipher if revert_char(c))
