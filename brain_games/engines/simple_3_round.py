from prompt import string as get_str

TURNS_COUNT = 3


def welcome(game_rules):
    print("Welcome to Brain Games!")
    print(game_rules)


def ask_name():
    return get_str("May I have your name? ")


def greet(name):
    print(f"Hello, {name}!")


def play_game(name, get_turn_cond):
    for _ in range(TURNS_COUNT):
        rslt = make_turn(get_turn_cond)
        if not rslt[0] == rslt[1]:
            print(f"'{rslt[0]}' is wrong answer ;(. Correct answer was '{rslt[1]}'.")  # noqa: E501
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f"Congratulations, {name}!")


def make_game(game):
    welcome(game.RULES_TEXT)
    print()
    name = ask_name()
    greet(name)
    print()
    play_game(name, game.get_turn_cond)


def make_turn(get_turn_cond):
    quest_text, correct_answer = get_turn_cond()
    print(f"Question: {quest_text}")
    players_answer = get_str("Your answer: ")
    return (players_answer, str(correct_answer))
