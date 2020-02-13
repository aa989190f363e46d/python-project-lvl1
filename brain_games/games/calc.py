from random import randint, choice
from operator import add, sub, mul

from sys import maxsize
from math import log2

TURNS_COUNT = 3
MAXINT = log2(maxsize) * 2 + 2
OPERATORS = {'+': add, '-': sub, '*': mul}

RULES_TEXT = "What is the result of the expression?"


def get_turn_cond():
    x, y = randint(1, MAXINT), randint(1, MAXINT)
    op = choice(list(OPERATORS.keys()))
    return (f"{x} {op} {y}",
            OPERATORS[op](x, y))
