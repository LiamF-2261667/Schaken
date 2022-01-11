from colorama import Fore
from Board import ClearBoard, DrawBoard
from Piece import SetPiece, RemovePiece, GetPieceColor

# Demo code
ClearBoard()

SetPiece(3, 7, "T", Fore.LIGHTWHITE_EX)
SetPiece(5, 6, "T", Fore.LIGHTWHITE_EX)
SetPiece(4, 5, "K", Fore.LIGHTWHITE_EX)
SetPiece(6, 4, "K", Fore.BLACK)

DrawBoard()

selected = input("Give the coordinate of the piece that should be selected: ")
print(selected)
