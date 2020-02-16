from random import randint

MAXINT = 100

RULES_TEXT = "Find the greatest common divisor of given numbers."


def gcd(x, y):
    v, u = min(x, y), max(x, y)
    while v:
        u, v = v, u % v
    return abs(u)


def get_turn_cond():
    x, y = randint(1, MAXINT), randint(1, MAXINT)
    return (f"{x} {y}",
            gcd(x, y))
