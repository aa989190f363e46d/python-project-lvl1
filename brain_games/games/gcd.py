from random import randint
from math import gcd

from sys import maxsize
from math import log2

MAXINT = log2(maxsize) * 2 + 2

RULES_TEXT = "Find the greatest common divisor of given numbers."


def get_turn_cond():
    x, y = randint(1, MAXINT), randint(1, MAXINT)
    return (f"{x} {y}",
            gcd(x, y))


def main():
    master.make_game(RULES_TEXT, get_turn_cond)


if __name__ == '__main__':
    from brain_games.games import master
    main()
