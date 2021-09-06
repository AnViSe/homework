#!/usr/bin/env python

r"""
Напишите функцию, которая генерирует вершины n-угольника.

Функция возвращает список вершин. Каждая вершина задаётся таплом из координат x и y.
Первая вершина лежит на оси Y: `(0.0, R)` (т.е. на 12 часов), следующие идут по часовой стрелке.

Например, квадрат будет иметь следующие 4 вершины:

`[(0.0, R), (R, 0.0), (0.0, -R), (-R, 0.0)]`


   1
  / \
 /   \
4     2
 \   /
  \ /
   3
"""


from math import pi, sin, cos

R = 3.0


def polygon_vertices(n: int, r: float = R) -> list:
    angle = pi / 2
    step = 2 * pi / n
    vertices = [(0.0, r)]

    for _ in range(n - 1):
        angle -= step
        vert = r * cos(angle), r * sin(angle)
        vertices.append(vert)

    return vertices