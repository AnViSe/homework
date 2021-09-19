#!/usr/bin/env python

"""
Даны два прямоугольника, стороны которых параллельны осям координат.
Известны координаты левого нижнего угла x, y, а также ширина и высота прямоугольника w, h.

                w
    ┌───────────────────────┐
    │                       │
    │                       │ h
    │                       │
    └───────────────────────┘
 (x, y)

- определить, принадлежат ли все точки второго прямоугольника первому (`all`).
- определить, пересекаются ли эти прямоугольники (`any`, `all`).
"""

from collections import namedtuple

Rect = namedtuple("Rect", "x y w h".split())


def to_set(z: Rect):
    return {(x, y) for x in range(z.x, z.w + 1) for y in range(z.y, z.h + 1)}


def rect_inside(a: Rect, b: Rect) -> bool:
    """
    Checks if whole rectangle `b` is within rectangle `a`.
    """
    ma = to_set(a)
    mb = to_set(b)
    mc = mb.difference(ma)
    return len(mc) == 0


def rects_intersect(a: Rect, b: Rect) -> bool:
    """
    Checks if 2 rectangles `a` and `b` have at least a single intersection point.
    """
    ma = to_set(a)
    mb = to_set(b)
    mc = ma.intersection(mb)
    return len(mc) > 0
