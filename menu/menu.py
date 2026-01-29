

from match import game
import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# Add path to parent directory to import from match package


def menu_text():  # menu for user input and what user wants to do, first thing user sees
    available_games_in_menu = ["Counter Strike 2",
                               "League Of Legends", "Inhouse Kapteenijaot"]
    print("Tervetuloa Pelipaja.net pelibottiin.")
    time.sleep(1)
    print("Valitse ennen mitä peliä varten haluat tehdä matsin.")
    time.sleep(1)
    print("\nKirjoita valinnan numero ja paina Enter.\n")
    print("1) Counter Strike 2")
    print("2) League of Legends")
    print("3) Lopeta")
    return available_games_in_menu


def get_game_selection():
    while True:
        os.system("cls")
        available_games_in_menu = menu_text()
        try:
            game_selection = int(input("Valitse Peli: "))
            if game_selection == 1:
                game.insertPlayers(game_selection)
            elif game_selection == 2:
                game.insertPlayers(game_selection)
            elif game_selection == 3:
                print("Valitsit Lopeta. Heihei!")
                exit()
            return game_selection
        except ValueError:
            print("\n Value Error: Virheellinen syöte, yritä uudelleen.")
            continue


def main():
    get_game_selection()


if __name__ == "__main__":
    main()
