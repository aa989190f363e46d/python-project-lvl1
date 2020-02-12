from brain_games.scripts.cli import welcome_user
from brain_games.games import master, even, calc, gcd, progression


def greeting():
    print("Welcome to the Brain Games!")
    print()


def main():
    greeting()
    welcome_user()


def play_even():
    master.make_game(even)


def play_calc():
    master.make_game(calc)


def play_gcd():
    master.make_game(gcd)


def play_progression():
    master.make_game(progression)


if __name__ == "__main__":
    main()
