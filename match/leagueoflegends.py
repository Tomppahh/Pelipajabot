import requests
import random
import os


def read_players_from_file(filename="players.txt"):
    players = []
    try:
        with open(filename, "r") as file:
            for line in file:
                player = line.strip()
                if player:  # Skip empty lines
                    players.append(player)

        if not players:
            print(f"Error: No players found in {filename}")
        return players

    except FileNotFoundError:
        print(f"Error: {filename} not found in directory {os.getcwd()}")
        return []
    except Exception as e:
        print(f"Error reading {filename}: {str(e)}")
        return []


class Game:
    def __init__(self, players_with_roles):
        self.PlayersWithRoles = players_with_roles


def fetch_players(game):
    return game.PlayersWithRoles


def fetch_champions() -> list:
    url = 'https://ddragon.leagueoflegends.com/cdn/13.1.1/data/en_US/champion.json'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return [champ['name'] for champ in data['data'].values()]
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return []


def select_random_champions(champions: list, num: int = 20) -> list:
    return random.sample(champions, num)


def display_champions(champion_list: list) -> None:
    print("Available Champions:")
    for index, champion in enumerate(champion_list):
        print(f"{index + 1}) {champion}")


def champion_auction(game):
    players = fetch_players(game)
    if not players:
        print("No players available for selection.")
        return {}

    champions = fetch_champions()
    if not champions:
        print("No champions fetched.")
        return {}

    selected_champions = select_random_champions(champions)
    champion_selection = {player: None for player in players}
    players_who_picked = []

    while len(players_who_picked) < len(players):
        random_player = random.choice(players)
        if random_player in players_who_picked:
            continue
        print(f"\nRandomly chosen player: {random_player}")
        display_champions(selected_champions)

        try:
            choice = int(input(
                f"\n{random_player}, choose a champion by number (1-{len(selected_champions)}): "))
            if 1 <= choice <= len(selected_champions):
                chosen_champion = selected_champions[choice - 1]
                champion_selection[random_player] = chosen_champion
                selected_champions.remove(chosen_champion)
                players_who_picked.append(random_player)
                print(f"{random_player} has chosen: {chosen_champion}")
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nAll players have chosen champions!")
    team1 = []
    team2 = []
    team_switch = 1  # Switch between Team 1 and Team 2

    for player, champion in champion_selection.items():
        if team_switch == 1:
            team1.append((player, champion))
            team_switch = 2
        else:
            team2.append((player, champion))
            team_switch = 1

    print("\nREADY TO START GAME! GOOD LUCK ON THE RIFT!\n")
    print(" Team 1 ".center(39, "=") + "|" + " Team 2 ".center(41, "="))
    print("=" * 39 + "|" + "=" * 41)

    for player1, player2 in zip(team1, team2):
        team1_text = f"{player1[0]}: {player1[1]}".ljust(39)
        team2_text = f"{player2[0]}: {player2[1]}".ljust(39)
        print(f"{team1_text}|   {team2_text}")
    print("=" * 81 + "\n")
    return champion_selection


def start_game(champion_selection):
    game_state = {
        "teams": {
            "Team 1": [],
            "Team 2": []
        },
        "status": "ongoing"
    }

    for index, (player, champion) in enumerate(champion_selection.items()):
        team = "Team 1" if index % 2 == 0 else "Team 2"
        game_state["teams"][team].append((player, champion))

    print("\nGame Start!")
    for team, members in game_state["teams"].items():
        print(f"{team}:")
        for player, champion in members:
            print(f"  {player}: {champion}")

    # Placeholder for game loop
    while game_state["status"] == "ongoing":
        pass


if __name__ == "__main__":
    # Read players from file
    players = read_players_from_file()

    if not players:
        print("Failed to start game due to missing players.")
        exit(1)

    game_instance = Game(players)
    selections = champion_auction(game_instance)
    start_game(selections)
