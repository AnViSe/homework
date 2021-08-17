#!/usr/bin/env python

# Бабушка Зина даёт своему любимому внуку Васе 3 монеты и разрешает оставить 2 из них.
# Найдите максимальную сумму из любых двух монет.
# Номинальная стоимость монет: a, b и с тугриков.
def max_sum_of_2(a: int, b: int, c: int) -> int:
    if (a + b) >= (b + c):
        r = (a + b)
    else:
        r = (b + c)
    if (a + c) >= r:
        r = (a + c)
    return r


if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    print(max_sum_of_2(a, b, c))
