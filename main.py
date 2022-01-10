from colorama import Fore, Back

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
                line += Back.LIGHTBLACK_EX + " " + chess_board[i][j] + " "
            else:
                line += Back.WHITE + " " + chess_board[i][j] + " "

        # De achtergrondkleur stop zetten en de verticale coordinaat toevoegen
        lineNumber = 8 - i
        line += Back.RESET + " " + str(lineNumber)

        # Het resultaat printen
        print (line)


# Een stuk op een specifieke plaats zetten
def SetPiece(horizontal, vertical, piece, color):
    hor = horizontal - 1
    ver = (8-vertical)
    chess_board[ver][hor] = color + piece + Fore.RESET


# Een stuk verwijderen van het bord
def RemovePiece(horizontal, vertical):
    hor = horizontal - 1
    ver = (8-vertical)
    chess_board[ver][hor] = " "


# Demo code
ClearBoard()

SetPiece(3, 7, "T", Fore.LIGHTWHITE_EX)
SetPiece(5, 6, "T", Fore.LIGHTWHITE_EX)
SetPiece(4, 5, "K", Fore.LIGHTWHITE_EX)
SetPiece(6, 4, "K", Fore.BLACK)

DrawBoard()
