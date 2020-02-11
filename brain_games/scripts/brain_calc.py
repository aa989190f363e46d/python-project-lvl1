from prompt import string as get_str
from random import randint, choice
from sys import maxsize
from operator import add, sub, mul
from math import log2

TURNS_COUNT = 3
MAXINT = log2(maxsize) * 2 + 2
OPERATORS = {'+': add, '-': sub, '*': mul}

def welcome(game_rules):
    print("Welcome to Brain Games!")
    print(game_rules)


def ask_name():
    return get_str("May I have your name? ")


def greet(name):
    print(f"Hello, {name}!")


def play_game(name):
    for _ in range(TURNS_COUNT):
        result = make_turn()
        if not result[0] == result[1]:
            print(f"'{result[0]}' is wrong answer ;(. Correct answer was '{result[1]}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f"Congratulations, {name}!")


def make_turn():
    x, y = randint(1, MAXINT), randint(1, MAXINT)
    op = choice(list(OPERATORS.keys())) 
    correct_answer = str(OPERATORS[op](x, y))
    print(f"Question: {x} {op} {y}")
    players_answer = get_str("Your answer: ")
    return (players_answer, correct_answer)

def main():
    rules_text = "What is the result of the expression?"
    welcome(rules_text)
    print()
    name = ask_name()
    greet(name)
    print()
    play_game(name)


if __name__ == '__main__':
    main()