from random import randint, choice

from sys import maxsize
from math import log2

TURNS_COUNT = 3
MAXINT = log2(maxsize) * 2 + 2
LENGTH = 10

RULES_TEXT = "What number is missing \033[1min the progression?"


def get_turn_cond():
    start, step = randint(1, MAXINT), randint(1, MAXINT // 10)
    seq = list(map(str, range(start, start + step * LENGTH, step)))
    correct_answer = choice(seq)
    seq[seq.index(correct_answer)] = '…'
    return (' '.join(seq),
            correct_answer)


def main():
    master.make_game(RULES_TEXT, get_turn_cond)


if __name__ == '__main__':
    from brain_games.games import master
    main()
