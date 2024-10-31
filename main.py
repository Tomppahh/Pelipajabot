from menu import *
from match import * 
import time
import platform
import os




def startupinfo():
    print("Starting Pelipaja Bot!")
    print("Python version", platform.python_version())
    print(f"System running {platform.system()}")
    time.sleep(3)
    os.system("cls") # clears terminal after time.sleep has passed




def main():
    startupinfo()
    menu.main()



if __name__ == "__main__":
    main()