from random import randint
from math import sqrt

from sys import maxsize
from math import log2

ANSWERS = ('no', 'yes')
MAXINT = log2(maxsize) * 2 + 2

RULES_TEXT = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."  # noqa: E501


def get_turn_cond():
    num = randint(1, MAXINT)
    correct_answer = ANSWERS[is_prime(num)]
    return (f"{num}", correct_answer)


def main():
    master.make_game(RULES_TEXT, get_turn_cond)


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    for i in range(5, int(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


if __name__ == '__main__':
    from brain_games.games import master
    main()
