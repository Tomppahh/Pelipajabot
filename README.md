# Pelipajabot
Pelipajabot is a terminal based old project of mine. It allows users to add 10 players to a text file and create 5v5 custom teams with other functionality based on the game choice. Current supported games are League of Legends and Counter Strike.


You can run the bot by downloading the files and running main.py file with command python main.py in the folder root file. 

If Counter-Strike is chosen, there are options for map-vetos and automatic setup with dathost.net server provider. The bot sends API calls to your server that you need to have setup in dathost after map has been selected, sending the selected map to server and starting the server if server is not already on. the bot then posts the connection info to the terminal for players to copy the connection information. 

If League of Legends is chosen, there are options to automatically assign roles for players from the basic LoL roles (TOP, JUNGLE, MID, ADC, SUPPORT) so you can make fun and random matchups with your friends. The bot is also able to fetch the current playable champion pool from the RIOT API and the bot user can choose to use the functionality that I named "Champion Auction". If this is enabled, players get to choose randomly in order a champion from a list of twenty random champions picked from the large pool of champions fetched from the API. This works even when random roles werent picked. So there are multiple options to create fun complete random games or just use the bot to assign captain options as in any other game. After everything is done the bot prints players in teams (and in roles if this was done) clearly to the user in terminal. then its just time to open the game and create a custom lobby and create a game based on these rules. League doesnt have a proper API way to create a custom game server so this part needs to be done manually.

You also need to create an apikey.py file to the root folder with following values:

RIOT_API_KEY = "your key here"
DATHOST_USERNAME = "your key here"
DATHOST_PASSWORD = "your key here"
SERVER_ID = "your key here"
CONNECTION_STRING = "your key here"

(replace "your key here" with your own information)

