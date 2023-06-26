#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


"""Скрипт для генерации похожих внешне слов."""


SIMILAR_SYMBOLS_LIST = [
    # ('B', 'E'),
    # ('B', 'H'),
    # ('B', 'K'),
    # ('B', 'O'),
    # ('B', 'P'),
    # ('C', 'O'),
    # ('C', 'Q'),
    # ('E', 'H'),
    # ('E', 'K'),
    # ('K', 'X'),
    # ('K', 'Y'),
    # ('M', 'X'),
    # ('M', 'Y'),
    # ('O', 'Q'),
    # ('U', 'Y'),
    # ('V', 'K'),
    # ('V', 'U'),
    # ('V', 'X'),
    # ('V', 'Y'),
    # ('a', 'c'),
    # ('a', 'e'),
    # ('a', 'o'),
    # ('a', 'p'),
    # ('b', 'c'),
    # ('b', 'e'),
    # ('b', 'o'),
    # ('b', 'p'),
    # ('c', 'e'),
    # ('c', 'o'),
    # ('e', 'o'),
    # ('k', 'x'),
    # ('k', 'y'),
    # ('o', 'p'),
    # ('x', 'y'),
    # ('Ё', 'E'),
    # ('Ё', 'H'),
    ("І", "T"),
    ("А", "A"),
    # ('Б', 'В'),
    # ('Б', 'B'),
    # ('В', 'Н'),
    # ('В', 'Ё'),
    ("В", "B"),
    # ('В', 'E'),
    # ('В', 'H'),
    # ('В', 'P'),
    # ('Е', 'Н'),
    # ('Е', 'Ё'),
    # ('Е', 'B'),
    ("E", "Е"),
    # ('Е', 'H'),
    # ('Ж', 'Х'),
    # ('Ж', 'K'),
    # ('Ж', 'X'),
    # ('Ж', 'Y'),
    # ('И', 'Й'),
    # ('И', 'H'),
    ("К", "K"),
    ("М", "M"),
    # ('Н', 'Ё'),
    # ('Н', 'E'),
    ("Н", "H"),
    # ('О', 'С'),
    ("О", "O"),
    # ('О', 'Q'),
    # ('Р', 'B'),
    ("Р", "P"),
    ("С", "C"),
    ("Т", "T"),
    # ('У', 'Ѵ'),
    # ('У', 'V'),
    # ('У', 'U'),
    # ('У', 'Y'),
    ("Х", "X"),
    # ('а', 'е'),
    # ('а', 'о'),
    # ('а', 'с'),
    # ('а', 'ё'),
    ("а", "a"),
    # ('а', 'c'),
    # ('а', 'e'),
    # ('а', 'o'),
    # ('в', 'е'),
    # ('в', 'н'),
    # ('в', 'ё'),
    # ('в', 'a'),
    # ('в', 'e'),
    # ('в', 'o'),
    # ('в', 'p'),
    # ('е', 'о'),
    # ('е', 'ё'),
    # ('е', 'a'),
    # ('е', 'c'),
    ("e", "е"),
    # ('е', 'o'),
    # ('и', 'й'),
    # ('и', 'м'),
    # ('о', 'a'),
    # ('о', 'b'),
    # ('о', 'c'),
    # ('о', 'e'),
    ("о", "o"),
    # ('о', 'p'),
    # ('р', 'c'),
    # ('р', 'o'),
    ("р", "p"),
    ("с", "c"),
    # ('с', 'e'),
    # ('с', 'o'),
    # ('с', 'p'),
    # ('у', 'Ѵ'),
    # ('у', 'V'),
    # ('у', 'K'),
    # ('у', 'X'),
    # ('у', 'Y'),
    ("у", "y"),
    # ('х', 'Ѵ'),
    # ('х', 'X'),
    # ('х', 'k'),
    ("х", "x"),
    # ('х', 'y'),
    # ('ё', 'e'),
    # ('ё', 'o'),
    # ('ё', 'p'),
    ("Ѵ", "V"),
    # ('Ѵ', 'U'),
    # ('Ѵ', 'Y'),
    # ('Ѵ', 'y'),
]

# TODO: временно, только для просмотра алгоритма
SIMILAR_SYMBOLS_DICT = {k: v for k, v in SIMILAR_SYMBOLS_LIST}
SIMILAR_SYMBOLS_DICT.update({v: k for k, v in SIMILAR_SYMBOLS_LIST})

text = "Привет! Большой тупой урод! Cat! Dog! Enot! gil9red! Big Nagibator! Zevs! "
new_text = "".join(SIMILAR_SYMBOLS_DICT.get(c, c) for c in text)

print(text)
print(new_text)
print()
number = 0
for i in range(len(text)):
    if text[i] != new_text[i]:
        number += 1
print(
    f"Изменено {number} символов (всего {len(text)} символов, прогресс {number / len(text):.0%})."
)
print(" ".join(f"{c: <3}" for c in text))
print(" ".join(f"{ord(c): <3x}" for c in text))

print()
print(" ".join(f"{c: <3}" for c in new_text))
print(" ".join(f"{ord(c): <3x}" for c in new_text))
