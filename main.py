from colorama import Fore
from Board import ClearBoard, DrawBoard
from Piece import SetPiece, RemovePiece, GetPieceColor
from Input import selectInput

# Demo code
ClearBoard()

SetPiece(3, 7, "T", Fore.BLUE)
SetPiece(5, 6, "T", Fore.BLUE)
SetPiece(4, 5, "K", Fore.BLUE)
SetPiece(6, 4, "K", Fore.BLACK)

DrawBoard()
selectInput()