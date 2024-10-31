import time
import os

def menu_text():  # menu for user input and what user wants to do, first thing user sees
    available_games_in_menu = ["Counter Strike 2", "League Of Legends", "Inhouse Kapteenijaot"]
    print("Tervetuloa Pelipaja.net pelibottiin.")
    time.sleep(1)
    print("Valitse ennen mitä peliä varten haluat tehdä matsin.")
    time.sleep(1)
    print("Kirjoita valinnan numero ja paina Enter.\n")
    print("1) Counter Strike 2")
    print("2) League of Legends")
    print("3) Haluan luoda XvX kapteenijaot") # kysyy pelaajien määrän per team
    print("4) Lopeta")
    return available_games_in_menu

def get_game_selection(): 
    available_games_in_menu = menu_text()
    while True:
        os.system("cls")
        menu_text()
        try:
            game_selection = int(input("Valitse Peli: "))
            if game_selection == 4:
                print("Valitsit Lopeta. Heihei!")
                exit()
            elif game_selection > 4 or game_selection < 1:
                print("\n Virheellinen valinta, yritä uudelleen.")
            else:
                print(f"MODE: {available_games_in_menu[game_selection - 1].upper()}")
            return game_selection
        except ValueError:
            print("\n Value Error: Virheellinen syöte, yritä uudelleen.")
            continue
        
        
    

            # pelaajat voi laittaa kaikki kerralla
        #tähän switch valikko rakenne ja suorita funktio riippuen pelistä  # Pelaajat numerovalikoidaan, valitse kapu tai random kapteenit
    os.system("cls") #clear screen
    print(f"***{game_selection}\n")




def menu_functionality(game, menu_selection):
    print()

def main():
    get_game_selection()


if __name__ == "__main__":
    main()
