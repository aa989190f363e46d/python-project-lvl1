from brain_games.engines.cli import welcome_to_game, ask_name, greet


def main():
    welcome_to_game('')
    greet(ask_name())


if __name__ == "__main__":
    main()
