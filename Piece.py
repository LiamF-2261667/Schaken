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

    elif chess_board[ver][hor].__contains__(Fore.BLUE):
        return "white"

    else:
        return "black"


def GetPieceType(horizontal, vertical):
    hor = horizontal - 1
    ver = (8-vertical)

    if chess_board[ver][hor] == " ":
        return "null"
        
    elif chess_board[ver][hor].__contains__("K"):
        return "King"
    elif chess_board[ver][hor].__contains__("Q"):
        return "Queen"
    elif chess_board[ver][hor].__contains__("B"):
        return "Bishop"
    elif chess_board[ver][hor].__contains__("H"):
        return "Horse"
    elif chess_board[ver][hor].__contains__("R"):
        return "Rook"
    elif chess_board[ver][hor].__contains__("P"):
        return "Pawn"

    else:
        return "404"