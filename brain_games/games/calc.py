from random import randint, choice
from operator import add, sub, mul

MAXINT = 100
OPERATORS = (('+', add),
             ('-', sub),
             ('*', mul))

RULES_TEXT = "What is the result of the expression?"


def get_turn_cond():
    x, y = randint(1, MAXINT), randint(1, MAXINT)
    op_name, op_fun = choice(OPERATORS)
    return (f"{x} {op_name} {y}",
            op_fun(x, y))
