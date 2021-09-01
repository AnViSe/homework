#!/usr/bin/env python

"""
Напишите программу, которая использует шахматную нотацию Форсайта-Эдвардса (FEN -  )
для подсчёта баланса материала между белыми и чёрными.

- https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation
- https://ru.wikipedia.org/wiki/Нотация_Форсайта_—_Эдвардса
- https://www.chessprogramming.org/Forsyth-Edwards_Notation

FEN задаёт полное расположение фигур на доске.
Относительная ценность фигур задана константами.
"""

PAWN_VAL = 1  # пешка
KNIGHT_VAL = BISHOP_VAL = 3  # конь и слон
ROOK_VAL = 5  # ладья
QUEEN_VAL = 9  # ферзь


def get_char_value(c: str) -> int:
    """Получение ценности одной фигуры"""
    # k - коэффициент
    # для белых = 1, для черных = -1, для остальных = 0
    k = c.isupper() - c.islower()
    # Определяем ценность фигуры от ее вида и цвета
    if c in 'pP':
        return PAWN_VAL * k
    elif c in 'rR':
        return ROOK_VAL * k
    elif c in 'bnBN':
        return KNIGHT_VAL * k
    elif c in 'qQ':
        return QUEEN_VAL * k
    else:
        return 0


def calc_chess_balance(fen: str) -> int:
    result = 0
    # Отбираем только позиции фигур
    lines = fen.split(' ')[0]
    # Перебираем посимвольно
    for c in lines:
        # Подсчитываем общую ценность фигур
        result = result + get_char_value(c)
    return result
