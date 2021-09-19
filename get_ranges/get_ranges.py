#!/usr/bin/env python

"""
Реализовать функцию `get_ranges` которая “сворачивает” список неповторяющихся целых чисел,
отсортированных по возрастанию:

- [0, 1, 2, 3, 4, 7, 8, 10] -> "0-4, 7-8, 10"
- [4, 7, 10] -> "4, 7, 10"
- [2, 3, 8, 9]) -> "2-3, 8-9"
"""


def get_ranges(l: list) -> str:
    result = []
    _range = []

    def append_to_result(e=[]):
        if e:
            result.append(f'{e[0]}-{e[-1]}' if e[0] != e[-1] else f'{e[0]}')

    for i in range(len(l)):
        if _range:
            if _range[-1] + 1 != l[i]:
                append_to_result(_range)
                _range.clear()
        _range.append(l[i])

    append_to_result(_range)

    return ", ".join(result)
