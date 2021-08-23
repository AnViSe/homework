#!/usr/bin/env python

"""
В школе, в которой учится В. Пупкин, занятия начинаются в 8 утра.
Урок длится 45 минут.
После каждого нечётного урока (1-го, 3-го, 5-го ...) перемена 5 минут,
а после каждого чётного (2-го, 4-го, 6-го ...) - 15.

Помогите непоседе Васе посчитать, когда заканчивается n-ый урок.
"""


def end_of_lesson(n: int) -> (int, int):
    all_minutes = 8 * 60  # Общее количество минут
    # С помощью for и range
    for i in range(1, n + 1):  # Перебираем уроки от 1 до n
        all_minutes += 45  # Добавляем длительность урока к общей длительности
        if i < n:  # Если это не последний урок
            if i % 2 == 0:  # Для четного урока
                all_minutes += 15
            else:  # Для нечетного урока
                all_minutes += 5
    # С помощью while
    # i = 1
    # while i <= n:
    #     all_minutes += 45
    #     if i < n:
    #         if i % 2 == 0:
    #             all_minutes += 15
    #         else:
    #             all_minutes += 5
    #     i += 1

    end_hours = all_minutes // 60  # Количество часов
    end_minutes = all_minutes % 60  # Количество минут
    return end_hours, end_minutes


if __name__ == "__main__":
    n = int(input("Номер урока: "))

    hours, minutes = end_of_lesson(n)

    print(f"{n}-ый урок заканчивается в {hours}:{minutes:02}")
