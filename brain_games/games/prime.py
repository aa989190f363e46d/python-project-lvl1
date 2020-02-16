from random import randint
from math import sqrt

MAXINT = 500

RULES_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501


def get_turn_cond():
    num = randint(1, MAXINT)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return (f"{num}", correct_answer)


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
