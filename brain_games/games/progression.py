from random import randint, choice

from sys import maxsize
from math import log2

MAXINT = log2(maxsize) * 2 + 2
LENGTH = 10

RULES_TEXT = "What number is missing \033[1min\033[0m the progression?"


def get_turn_cond():
    start, step = randint(1, MAXINT), randint(1, MAXINT // 10)
    seq = list(map(str, range(start, start + step * LENGTH, step)))
    correct_answer = choice(seq)
    seq[seq.index(correct_answer)] = '…'
    return (' '.join(seq),
            correct_answer)
