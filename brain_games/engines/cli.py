from prompt import string as get_str


def welcome_to_game(game_rules):
    print("Welcome to Brain Games!")
    print(game_rules)


def ask_name():
    return get_str("May I have your name? ")


def greet(name):
    print(f"Hello, {name}!")


def welcome_user():
    name = ask_name()
    greet(name)
