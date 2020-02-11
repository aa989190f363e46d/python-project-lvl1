from prompt import string as get_str
from random import randint
from sys import maxsize

TURNS_COUNT = 3
ANSWERS = ('no', 'yes')
MAXINT = maxsize * 2 + 2

def welcome():
    print("Welcome to Brain Games!")
    print("Answer \"yes\" if number even otherwise answer \"no\".")


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
    num = randint(1,MAXINT)
    correct_answer = ANSWERS[num % 2 == 0]
    print(f"Question: {num}")
    players_answer = get_str("Your answer: ")
    return (players_answer, correct_answer)

def main():
    welcome()
    print()
    name = ask_name()
    greet(name)
    print()
    play_game(name)


if __name__ == '__main__':
    main()