from random import randint

MAXINT = 100

RULES_TEXT = 'Answer "yes" if number even otherwise answer "no".'


def get_turn_cond():
    num = randint(1, MAXINT)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return (f"{num}", correct_answer)
