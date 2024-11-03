import random

class Game:
    leagueMaps = ["Summoners Rift", "Howling Abyss"]
    playerlist = []
    chosen_playerlist = []
    captain1 = ""
    captain2 = ""
    team_size = 5
    team1 = []
    team2 = []

    def CoinFlip(self):
        coinflip = ["team1", "team2"]
        result = random.coinflip
        return result

    def __init__(self):
        self.file_path = "maps.txt"
        self.maps = self.readMapsFile()

    def readMapsFile(self):
        try:
            with open(self.file_path, "r") as file:
                all_maps = file.readlines()
                maps = []

                for i in range(len(all_maps)):
                    map = all_maps[i].split()
                    maps.extend(map)
            return maps
        except FileNotFoundError:
            print("Error in maps.txt file, map not found.")
            return [] # Jos ois kaatumassa, palauta tyhjä lista.

def insertPlayers():
    team_size = int(input("Please insert team size: "))
    n = 0
    while n < team_size*2:
        player = input(f"Add player {n+1}: ")
        Game.playerlist.append(player)
        n += 1
        
def choosePlayers():
    playerlist = Game.playerlist
    chosen_playerlist = Game.chosen_playerlist
    print("would you like to shuffle teams or use captains?")
    print("1) Shuffle teams")
    print("2) Captains")
    choice = input("Choose option: ")
    if choice == "1":
       Game.team1.append = random.sample(playerlist)
       chosen_playerlist.append(playerlist)
       playerlist.remove(Game.team1)
       Game.team2.append = playerlist
       playerlist.remove(Game.team2)
    elif choice == "2":
        # give each player number value and list players
        for index, player in enumerate(playerlist, start=1):
            print(f"{index}) {player}")
        while len(playerlist > 0):
            choice = int(input("Select player by number: "))
            if 1 <= choice <= len(playerlist):
                selected_player = playerlist [choice - 1]
                print(f"You selected: {selected_player}")
                playerlist.remove(selected_player)
                chosen_playerlist.append(selected_player)
            else:
                print("Invalid choice. Input menu number, not player name.")
        print("All players have been chosen from the playerlist.")
    
    

def Captains():
    playerlist = Game.playerlist
    chosen_playerlist = Game.chosen_playerlist
    captain1 = Game.captain1
    captain2 = Game.captain2
    
    n = 0
    print(f"Player list has {len(Game.playerlist)} players: ")
    # listaan numerot ja voi painaa valikosta numeroa valitakseen pelaajan!
    for player in Game.playerlist:
        print(player)
    
