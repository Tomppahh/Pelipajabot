import random
from . import leagueoflegends as lol
from . import counterstrike as cs


class Game:
    leagueRoles = ["Top", "Jungle", "Mid", "ADC", "Support"]
    PlayersWithRoles = []
    CS2maps = []
    playerlist = []
    chosen_playerlist = []
    captain1 = ""
    captain2 = ""
    team_size = 5
    Team1 = []
    Team2 = []
    maps_file_path = "maps.txt"
    players_file_path = "players.txt"

    @classmethod
    def insert_players(cls, players):
        cls.PlayersWithRoles = players


def readFiles():
    try:
        Game.CS2maps.clear()
        Game.playerlist.clear()

        with open(Game.maps_file_path, "r") as maps_file:
            Game.CS2maps = maps_file.read().splitlines()

        with open(Game.players_file_path, "r", encoding="utf-8") as players_file:
            Game.playerlist = players_file.read().splitlines()

    except FileNotFoundError as e:
        print(f"Error: {e}")

    # DEBUG PRINTS
    # print("Maps:", Game.CS2maps)
    # print("Players:", Game.playerlist)


def CoinFlip():
    coinflip = ["Team 1", "Team 2"]
    result = random.choice(coinflip)
    print(f"\nCoinflip result: {result} starts the pick")
    return result


def insertPlayers(game_selection):
    readFiles()
    print("")
    if len(Game.playerlist) == 0:
        Game.team_size = int(input("Please insert team size: "))
        n = 0
        while n < Game.team_size * 2:
            player_input = input(f"Add player {n+1}: ")
            if "," in player_input:
                players = [name.strip() for name in player_input.split(",")]
                for player in players:
                    if n >= Game.team_size * 2:
                        break
                    Game.playerlist.append(player)
                    n += 1
            else:
                Game.playerlist.append(player_input.strip())
                n += 1
    else:
        print("Players in players.txt detected. Loading player list!")
    choosePlayers(game_selection)


def assignRandomRoles(team):
    random_roles = random.sample(Game.leagueRoles, len(team))
    return [f"{player} ({role})" for player, role in zip(team, random_roles)]


def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().upper()
        if response in ("Y", "N"):
            return response
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")


def sort_team_by_role(team):
    role_order = ["Top", "Jungle", "Mid", "ADC", "Support"]

    def role_key(player_with_role):
        role_part = player_with_role.split(
            '(')[-1]
        role = role_part.strip(')')

        if role in role_order:
            return role_order.index(role)  # Get the index if role is found
        else:
            return len(role_order)  # Default to the end if role is not found

    # Sort the team using the defined key
    sorted_team = sorted(team, key=role_key)
    return sorted_team


def choosePlayers(game_selection):
    result = CoinFlip()
    team_switch = 1 if result == "Team1" else -1
    team_number = 1 if team_switch == 1 else 2
    playerlist = Game.playerlist
    chosen_playerlist = Game.chosen_playerlist
    print("Would you like to shuffle teams or use captains?")
    print("1) Shuffle teams")
    print("2) Captains")
    choice = input("\nChoose option: ")

    if choice == "1":
        chosen_players = random.sample(playerlist, Game.team_size)
        Game.Team1.extend(chosen_players)

        for player in chosen_players:
            playerlist.remove(player)

        Game.Team2.extend(playerlist)

    elif choice == "2":
        Captains()
        print(
            f"\nStarting team selection with Captain {Game.captain1 if team_switch == 1 else Game.captain2} based on the coin flip.\n")
        while len(playerlist) > 0:
            current_captain = Game.captain1 if team_switch == 1 else Game.captain2
            print(f"{current_captain}'s turn to pick. (Team {team_number})")
            print("Available players:")
            for index, player in enumerate(playerlist, start=1):
                print(f"{index}) {player}")

            selection = input(
                f"Team {current_captain} (Team {team_number}), select player by number (or type 'restart' to restart): ")
            if selection.lower() == 'exit':
                # Restore playerlist to its original state
                playerlist.extend(chosen_playerlist)
                Game.Team1.clear()
                Game.Team2.clear()
                print("Player selection exited and lists restored. Restarting.")
                choosePlayers()
                return

            try:
                choice = int(selection)
                if 1 <= choice <= len(playerlist):
                    selected_player = playerlist[choice - 1]
                    print(f"You selected: {selected_player}")
                    if team_switch == 1:
                        Game.Team1.append(selected_player)
                    else:
                        Game.Team2.append(selected_player)
                    chosen_playerlist.append(selected_player)
                    playerlist.remove(selected_player)
                    team_switch *= -1  # Switch turn to the other captain
                    team_number = 1 if team_switch == 1 else 2
                else:
                    print("Invalid choice. Choose a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a valid number or 'exit'.")
    # if game is league (2)
    if game_selection == 2:
        do_random_roles = get_yes_no_input(
            "Assign random roles as well? Y/N: ")
        if do_random_roles.upper() == "Y":
            Game.Team1 = assignRandomRoles(Game.Team1)
            Game.Team2 = assignRandomRoles(Game.Team2)

            # Sort teams by role
            Game.Team1 = sort_team_by_role(Game.Team1)
            Game.Team2 = sort_team_by_role(Game.Team2)
    # make a player & rolelist to send to leagueoflegends.py
    # print out teams
    print("\nAll players have been chosen from the playerlist.")
    print("\nREADY TO START GAME! GOOD LUCK!\n")
    print("Team 1:                   Team 2:")
    for player1, player2 in zip(Game.Team1, Game.Team2):
        print(f"{player1:<25} {player2}")
        Game.PlayersWithRoles.append(player1)
        Game.PlayersWithRoles.append(player2)
    print("")
    if game_selection == 2:
        Game.insert_players(Game.PlayersWithRoles)
        # Pass the Game object to champion_auction
        lol.champion_auction(Game)
    elif game_selection == 1:
        cs.mapVeto(result)
    return result


def Captains():
    playerlist = Game.playerlist
    chosen_playerlist = Game.chosen_playerlist

    for n in range(1, 3):  # Loop for two captains
        print("Available players:")
        for index, player in enumerate(playerlist, start=1):
            print(f"{index}) {player}")

        while True:
            try:
                print("Random captain: "+random.choice(playerlist))
                menuchoice = int(input(f"Choose captain {n} by number: "))
                if menuchoice == 0:  # Random captain selection
                    # Random captain selection logic goes here
                    break
                elif 1 <= menuchoice <= len(playerlist):
                    # Get the actual player name
                    selected_player = playerlist[menuchoice - 1]
                    print(f"You selected: {selected_player}")

                    if n == 1:
                        Game.captain1 = selected_player
                        Game.Team1.append(selected_player)
                    elif n == 2:
                        Game.captain2 = selected_player
                        Game.Team2.append(selected_player)

                    # Remove the selected player from the playerlist and add to chosen_playerlist
                    playerlist.remove(selected_player)
                    chosen_playerlist.append(selected_player)
                    break  # Exit the loop after a valid selection
                else:
                    print("Invalid choice. Please choose a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
