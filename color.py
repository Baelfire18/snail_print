"""
This file has a feature in progress
"""


class bcolors:
    PURPLE = "\033[95m"
    ORANGE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    NORMAL = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


if __name__ == "__main__":
    print(f"{bcolors.PURPLE}Hello{bcolors.NORMAL}")
    print(f"{bcolors.ORANGE}Hello{bcolors.NORMAL}")
    print(f"{bcolors.CYAN}Hello{bcolors.NORMAL}")
    print(f"{bcolors.GREEN}Hello{bcolors.NORMAL}")
    print(f"{bcolors.YELLOW}Hello{bcolors.NORMAL}")
    print(f"{bcolors.RED}Hello{bcolors.NORMAL}")
    print(f"{bcolors.BOLD}Hello{bcolors.NORMAL}")
    print(f"{bcolors.UNDERLINE}Hello{bcolors.NORMAL}")
