#!/usr/bin/env python

"""
Напишите функцию, которая находит n наиболее употребляемых слов из Библии.
Слова в возвращаемом списке идут по убыванию их частоты использования.
"""
import string
from pathlib import Path

f = Path(__file__).parent.absolute() / "king_james_bible.txt"
BIBLE = f.read_text()


def most_freq_bible_words(n: int) -> list:
    worlds = {}
    items = BIBLE.split()
    for item in items:
        if item[-1] in string.punctuation:
            item = item[0: -1]
        world = item.lower()
        world_count = worlds.get(world, 0)
        world_count += 1
        worlds.update({world: world_count})

    result = [i for i, _ in sorted(worlds.items(), key=lambda i: i[1], reverse=True)]
    return result[0: n]


if __name__ == "__main__":
    print(*most_freq_bible_words(10), sep="\n")
