from colorama import Fore, Back

def title():
    print(Back.WHITE + Fore.BLACK)
    print("   _____ _    _ ______  _____ _____  ")
    print("  / ____| |  | |  ____|/ ____/ ____| ")
    print(" | |    | |__| | |__  | (___| (___   ")
    print(" | |    |  __  |  __|  \___ \\___  \  ")
    print(" | |____| |  | | |____ ____) |___) | ")
    print("  \_____|_|  |_|______|_____/_____/  ")
    print("                                     ")
    print(Back.RESET + Fore.RESET)


def help():
    print(Back.WHITE + Fore.BLACK)
    print("                                     ")
    print("  Invoer                             ")
    print(" ----------------------------------- ")
    print("  Om een coordinaat in te voeren     ")
    print("  geeft u eerst de letter en daarna  ")
    print("  het cijfer, bv: d5                 ")
    print("                                     ")
    print(Back.RESET + Fore.RESET)


def legende():
    print(Back.WHITE + Fore.BLACK)
    print("                                     ")
    print("  Legende                            ")
    print(" ----------------------------------- ")
    print("  P = Pawn   |  Pion                 ")
    print("  R = Rook   |  Toren                ")
    print("  H = Horse  |  Paard                ")
    print("  B = Bishop |  Loper                ")
    print("  Q = Queen  |  Koningin             ")
    print("  K = King   |  Koning               ")
    print("                                     ")
    print(Back.RESET + Fore.RESET)