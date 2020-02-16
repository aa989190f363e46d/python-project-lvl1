from brain_games.games import progression
from brain_games.engines import simple_3_round as master


def main():
    master.play_game(progression)


if __name__ == "__main__":
    main()
