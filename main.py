from os import system
from colorama import Fore

import intro
from Board import DrawBoard
from Piece import SetPiece, PieceColorToCode
from Input import selectInput, destinationInput

# Intro
intro.title()
intro.help()
intro.legende()
input("Druk op ENTER om verder te gaan... ")

# Alle stukken plaatsen
SetPiece(1, 1, "R", Fore.BLUE)
SetPiece(2, 1, "H", Fore.BLUE)
SetPiece(3, 1, "B", Fore.BLUE)
SetPiece(4, 1, "K", Fore.BLUE)
SetPiece(5, 1, "Q", Fore.BLUE)
SetPiece(6, 1, "B", Fore.BLUE)
SetPiece(7, 1, "H", Fore.BLUE)
SetPiece(8, 1, "R", Fore.BLUE)

for i in range(1, 9):
    SetPiece(i, 2, "P", Fore.BLUE)

SetPiece(1, 8, "R", Fore.RED)
SetPiece(2, 8, "H", Fore.RED)
SetPiece(3, 8, "B", Fore.RED)
SetPiece(4, 8, "K", Fore.RED)
SetPiece(5, 8, "Q", Fore.RED)
SetPiece(6, 8, "B", Fore.RED)
SetPiece(7, 8, "H", Fore.RED)
SetPiece(8, 8, "R", Fore.RED)

for i in range(1, 9):
    SetPiece(i, 7, "P", Fore.RED)

# Het bord tekenen
system("clear")
DrawBoard()

# De game loop
turn = "white"

while True:
    print("De beurt is aan " + PieceColorToCode(turn) + turn + "!" + Fore.RESET)

    # Als het selecteren van een stuk lukt
    if selectInput(turn) == True:
        print("")

        # Als het verplaatsen van een stuk lukt
        if destinationInput() == True:
            # De beurt veranderen
            if turn == "white": 
                print("turn should now become black")
                turn = "black"
                
            elif turn == "black": 
                print("turn should now become white")
                turn = "white"

            # Clear de console
            system("clear")

            # Tekenen het bord met de aanpassing
            DrawBoard()
            
        else:
            print("")

    else:
        print("")


# TODO:
# ------------------------------------------
# + En passant legaal maken
# + Pionen promoveren
# 
# + Schaak prioritizeren voor andere stukken mogen bewegen
# + Zorgen dat je jezelf niet schaak zet als je een stuk beweegt
# 
# + Schaakmat / pad
# + Het spel beïndigen en winnaar geven
# 