from colorama import Fore
from Board import DrawBoard
from Piece import SetPiece
from Input import selectInput, destinationInput

# Demo code
SetPiece(3, 7, "R", Fore.BLUE)
SetPiece(5, 6, "R", Fore.BLUE)
SetPiece(4, 5, "K", Fore.BLUE)
SetPiece(6, 4, "K", Fore.RED)

DrawBoard()


def movePiece():
    if selectInput() == True:
        print("")

        destinationInput()
        movePiece()

    else:
        print("")
        
        movePiece()


movePiece()
