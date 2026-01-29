from menu import menu
import time
import platform
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'match'))


def startupinfo():
    print("Starting Pelipaja Bot!")
    print("Python version", platform.python_version())
    print(f"System running {platform.system()}")
    time.sleep(1)
    os.system("cls")  # clears terminal after time.sleep has passed


def main():
    startupinfo()
    menu.main()


if __name__ == "__main__":
    main()
