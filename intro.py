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

