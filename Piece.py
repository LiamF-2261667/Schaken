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

    return PieceCodeToColor(chess_board[ver][hor])


# Bepalen welk stuk op een bepaald coordinaat staat
def GetPieceType(horizontal, vertical):
    hor = horizontal - 1
    ver = (8-vertical)

    if chess_board[ver][hor] == " ":
        return "null"
        
    name = PieceLetterToName(chess_board[ver][hor])
    
    if name == "null":
        return "404"
    
    else:
        return name


# Functie om een letter naar de volledige naam om te zetten
def PieceLetterToName(letter):
    if letter.__contains__("K"):
        return "King"
    elif letter.__contains__("Q"):
        return "Queen"
    elif letter.__contains__("B"):
        return "Bishop"
    elif letter.__contains__("H"):
        return "Horse"
    elif letter.__contains__("R"):
        return "Rook"
    elif letter.__contains__("P"):
        return "Pawn"

    else:
        return "null"


# Functie om de volledige naam om te zetten naar de letter op het bord
def PieceNameToLetter(name):
    if name.__contains__("King"):
        return "K"
    elif name.__contains__("Queen"):
        return "Q"
    elif name.__contains__("Bishop"):
        return "B"
    elif name.__contains__("Horse"):
        return "H"
    elif name.__contains__("Rook"):
        return "R"
    elif name.__contains__("Pawn"):
        return "P"

    else:
        return "null"


# Functie om de kleurnaam om te zetten in bruikbare code
def PieceColorToCode(color):
    if color == "white":
        return Fore.BLUE
    elif color == "black":
        return Fore.RED
    
    else:
        return "null"


# Functie om de kleurcode om te zetten naar een string
def PieceCodeToColor(code):
    if code.__contains__(Fore.BLUE):
        return "white"
    elif code.__contains__(Fore.RED):
        return "black"

    else:
        return "null"