from colorama import Fore
from Board import chess_board


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


# Bepalen of een stuk bestaat op een bepaald coordinaat en of het tot zwart of wit behoord
def GetPieceColor(horizontal, vertical):
    hor = horizontal - 1
    ver = (8-vertical)

    if chess_board[ver][hor] == " ":
        return "null"

    elif chess_board[ver][hor].__contains__(Fore.LIGHTWHITE_EX):
        return "white"

    else:
        return "black"