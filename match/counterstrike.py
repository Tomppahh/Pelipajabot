import apikey
from match import game
import requests
import dathost
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def readFiles():
    try:
        game.Game.CS2maps.clear()
        game.Game.playerlist.clear()

        with open(game.Game.maps_file_path, "r") as maps_file:
            game.Game.CS2maps = maps_file.read().splitlines()

    except FileNotFoundError as e:
        print(f"Error: {e}")

    print("(counterstrike.py) Maps:", game.Game.CS2maps)


def dathost(selected_map):

    DATHOST_USERNAME = apikey.DATHOST_USERNAME
    DATHOST_PASSWORD = apikey.DATHOST_PASSWORD
    SERVER_ID = apikey.SERVER_ID

    print(" DEBUG: SELECTED MAP IS: ", selected_map)
    connection_string = apikey.CONNECTION_STRING

    try:
        server_response = requests.get(
            f"https://dathost.net/api/0.1/game-servers/{SERVER_ID}",
            auth=(DATHOST_USERNAME, DATHOST_PASSWORD)
        )

        if server_response.status_code != 200:
            print(f"Error retrieving server status: {server_response.text}")
            return connection_string

        server = server_response.json()

        if selected_map:
            try:
                map_update = requests.put(
                    f"https://dathost.net/api/0.1/game-servers/{SERVER_ID}",
                    auth=(DATHOST_USERNAME, DATHOST_PASSWORD),
                    files={
                        "cs2_settings.game_mode": (None, "competitive"),
                        "cs2_settings.maps_source": (None, "mapgroup"),
                        "cs2_settings.mapgroup_start_map": (None, selected_map)
                    }
                )
                print(f"\nSetting server map to {selected_map}...")
            except:
                print(
                    "Error occurred while setting the server map. (line 47 counterstrike.py)")
            if map_update.status_code != 200:
                print(f"Error updating map: {map_update.text}")
            else:
                print(f"Map successfully set to {selected_map}")

        if not server.get("on", False):
            print("\nServer is not running. Starting server...")
            start_response = requests.post(
                f"https://dathost.net/api/0.1/game-servers/{SERVER_ID}/start",
                auth=(DATHOST_USERNAME, DATHOST_PASSWORD)
            )

            if start_response.status_code != 200:
                print(f"Error starting server: {start_response.text}")
            else:
                print("Server started successfully!")
        else:
            print("\nServer is already running.")

        print(f"\nServer connection info: {connection_string}")
        return connection_string

    except Exception as e:
        print(f"Error connecting to Dathost API: {str(e)}")
        return connection_string


def mapVeto(result):

    current_team = "Team 2" if result == "Team 1" else "Team 1"

    maps = game.Game.CS2maps.copy()

    if len(maps) == 0:
        print("Error: No maps available for veto. Please add maps to maps.txt")
        return

    print("\n===== MAP VETO PROCESS =====")
    print(f"{current_team} starts banning (lost the coinflip)")

    # Continue banning until only one map remains
    while len(maps) > 1:
        print(f"\n{current_team}'s turn to ban a map:")
        print("Available maps:")
        for i, map_name in enumerate(maps, 1):
            print(f"{i}. {map_name}")

        while True:
            try:
                choice = int(
                    input(f"{current_team}, choose a map to ban (1-{len(maps)}): "))
                if 1 <= choice <= len(maps):
                    banned_map = maps.pop(choice - 1)
                    print(f"{current_team} banned: {banned_map}")
                    break
                else:
                    print(
                        f"Invalid choice. Please enter a number between 1 and {len(maps)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        current_team = "Team 2" if current_team == "Team 1" else "Team 1"

    final_map = maps[0]
    print("\n===== VETO COMPLETE =====")
    print(f"The selected map is: {final_map}")
    print("Good luck and have fun!")
    print("Connecting to server...")
    connection_string = dathost(final_map)
    print(
        f"Connection string: {connection_string} has been setup with map {final_map}")
    print("Server is ready for players to join.")
    return final_map


if __name__ == "__main__":
    readFiles()
