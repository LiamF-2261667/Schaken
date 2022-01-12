from colorama import Back, Style

# Het aanmaken van de "schaakbord"-matrix
chess_board = [[" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "]]


# Het schaakbord volledig leegmaken
def ClearBoard():
    global chess_board
    chess_board = [[" ", " ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " ", " "]]


# Het bord tekenen met elk stuk
def DrawBoard():
    # Horizontale coordinaten
    print (" A  B  C  D  E  F  G  H ")

    # Uitvoeren voor elke rij
    for i in range(0,8):
        line = ""

        # Bepalen of het vakje donker of licht gekleurd moet zijn
        for j in range(0,8):
            if (i+j) % 2 == 0:
                line += Back.WHITE + Style.BRIGHT + " " + chess_board[i][j] + " "
            else:
                line += Back.LIGHTBLACK_EX + Style.BRIGHT + " " + chess_board[i][j] + " "

        # De achtergrondkleur stop zetten en de verticale coordinaat toevoegen
        lineNumber = 8 - i
        line += Back.RESET + " " + str(lineNumber)

        # Het resultaat printen
        print(line)
        
    print("")
