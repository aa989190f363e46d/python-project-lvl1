from brain_games.games import calc
from brain_games.engines import simple_3_round as master


def main():
    master.play_game(calc)


if __name__ == "__main__":
    main()
