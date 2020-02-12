from random import randint
from sys import maxsize

ANSWERS = ('no', 'yes')
MAXINT = maxsize * 2 + 2

RULES_TEXT = "Answer \"yes\" if number even otherwise answer \"no\"."


def get_turn_cond():
    num = randint(1, MAXINT)
    correct_answer = ANSWERS[num % 2 == 0]
    return (f"{num}", correct_answer)


def main():
    master.make_game(RULES_TEXT, get_turn_cond)


if __name__ == '__main__':
    from brain_games.games import master
    main()
