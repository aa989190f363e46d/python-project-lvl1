from prompt import string as get_str

from brain_games.engines.cli import welcome_to_game, ask_name, greet

TURNS_COUNT = 3


def play_game(game):
    welcome_to_game(game.RULES_TEXT)
    print()
    name = ask_name()
    greet(name)
    print()
    for _ in range(TURNS_COUNT):
        quest_text, correct_answer = game.get_turn_cond()
        print(f"Question: {quest_text}")
        players_answer = get_str("Your answer: ")
        if not players_answer == str(correct_answer):
            print(f"'{players_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f"Congratulations, {name}!")
