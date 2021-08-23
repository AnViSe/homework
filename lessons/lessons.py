#!/usr/bin/env python

"""
В школе, в которой учится В. Пупкин, занятия начинаются в 8 утра.
Урок длится 45 минут.
После каждого нечётного урока (1-го, 3-го, 5-го ...) перемена 5 минут,
а после каждого чётного (2-го, 4-го, 6-го ...) - 15.

Помогите непоседе Васе посчитать, когда заканчивается n-ый урок.
"""


def end_of_lesson(n: int) -> (int, int):
    all_min = 8 * 60
    # С помощью for и range
    for i in range(1, n + 1):
        all_min += 45
        if i < n:
            if i % 2 == 0:
                all_min += 15
            else:
                all_min += 5
    # С помощью while
    # i = 1
    # while i <= n:
    #     all_min += 45
    #     if i < n:
    #         if i % 2 == 0:
    #             all_min += 15
    #         else:
    #             all_min += 5
    #     i += 1

    r_h = all_min // 60
    r_m = all_min % 60
    return r_h, r_m


if __name__ == "__main__":
    n = int(input("Номер урока: "))

    hours, minutes = end_of_lesson(n)

    print(f"{n}-ый урок заканчивается в {hours}:{minutes:02}")
