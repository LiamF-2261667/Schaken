from colorama import Fore

from Piece import GetPieceType, GetPieceColor, SetPiece, PieceNameToLetter, PieceColorToCode, RemovePiece, PieceCodeToColor
from Legalizing import isLegal, isKingInDanger
import Board


# Een functie om de letters om te zetten in cijfers
def letterToNumber(letter):
    if letter == 'A':
        return 1
    elif letter == 'B':
        return 2
    elif letter == 'C':
        return 3
    elif letter == 'D':
        return 4
    elif letter == 'E':
        return 5
    elif letter == 'F':
        return 6
    elif letter == 'G':
        return 7
    elif letter == 'H':
        return 8

    else:
        return "null"


# Een functie om een coordinaat aan de gebruiker te vragen
def coordToNumbersArray(prompt):
    # Aanvragen van de input en omzetten naar een array
    dest = list(input(prompt))

    if len(dest) != 2:
        print(Fore.RED + "Foutieve invoer, geef eerst de letter en daarna het cijfer in!" + Fore.RESET)
        return "null"

    # Letter in een hoofdletter zetten
    letter = str.capitalize(dest[0])
    # Testen of de eerste invoer daadwerkelijk een letter is
    if str.isalpha(letter) == False:
        print(Fore.RED + "Foutieve invoer, als eerste moet de letter gegeven worden!" + Fore.RESET)
        return "null"

    # Testen als de tweede invoer daadwerkelijk een cijfer is en omzetten van een string naar een integer
    try: 
      number = int(dest[1])
    except ValueError:
      print(Fore.RED + "Foutieve invoer, als tweede moet het cijfer gegeven worden!" + Fore.RESET)
      return "null"
    
    # Selectie opslaan
    hor = letterToNumber(letter)
    ver = number

    # Testen als de invoer een coordinaat kan zijn
    if hor == "null":
        print(Fore.RED + "Deze letter behoord niet tot het schaakbord!" + Fore.RESET)
        return "null"
    
    if ver > 8:
        print(Fore.RED + "Dit nummer behoord niet tot het schaakbord!" + Fore.RESET)
        return "null"
    
    if ver < 1:
        print(Fore.RED + "Dit nummer behoord niet tot het schaakbord!" + Fore.RESET)
        return "null"
    
    # destination returnen
    return hor, ver, letter

selectedHor = 1
selectedVer = 1

# Het selecteren van een stuk (bv: A6)
def selectInput(currTeam):
    selected = coordToNumbersArray("Geef het coordinaat van het stuk dat u wilt selecteren: ")

    # Testen als de invoer correct was
    if selected == "null":
        return False

    hor = selected[0]
    ver = selected[1]
    letter = selected[2]

    # Testen als er een stuk daadwerkelijk is op deze positie
    if GetPieceType(hor, ver) == "null":
        print(Fore.RED + "Er staat geen stuk op deze positie" + Fore.RESET)
        return False
    
    if GetPieceType(hor, ver) == "404":
        print(Fore.RED + "ERROR: 404" + Fore.RESET)
        return False

    if GetPieceColor(hor, ver) != currTeam:
        print(Fore.RED + "Het is de beurt van " + currTeam + "!" + Fore.RESET)
        return False
    
    # De selectie globaal maken
    global selectedHor
    selectedHor = hor

    global selectedVer
    selectedVer = ver

    # Output
    print(Fore.LIGHTGREEN_EX + "Er staat een " + GetPieceColor(hor, ver) + " " + GetPieceType(hor, ver) + " op het coordinaat " + letter + str(ver) + Fore.RESET)
    
    return True


def destinationInput():
    dest = coordToNumbersArray("Geef het coordinaat van de gewenste verplaatsing: ")

    # Testen als de invoer correct was
    if dest == "null":
        return False
    
    hor = dest[0]
    ver = dest[1]

    # Informatie voor het nieuwe stuk verzamelen
    pieceTypeStr = GetPieceType(selectedHor, selectedVer)
    pieceType = PieceNameToLetter(pieceTypeStr)
    
    pieceColorStr = GetPieceColor(selectedHor, selectedVer)
    pieceColor = PieceColorToCode(pieceColorStr)

    # Kijken of de zet mogelijk is
    legality = isLegal(selectedHor, selectedVer, hor, ver, pieceType, pieceColorStr)
    if legality == "illegal":
        print(Fore.RED + "Deze zet is niet mogelijk!" + Fore.RESET)
        return False
    
    elif legality == "no movement":
        print(Fore.RED + "Het stuk staat al op deze plaats!" + Fore.RESET)
        return False
    
    elif legality == "taking self":
        print(Fore.RED + "Je kan niet een eigen stuk nemen!" + Fore.RESET)
        return False

    elif legality == "blocked":
        print(Fore.RED + "Er staat een stuk in de weg!" + Fore.RESET)
        return False

    Board.chess_board_BAK = Board.chess_board

    # Het oude stuk verwijderen en het nieuwe stuk plaatsen
    RemovePiece(selectedHor, selectedVer)

    SetPiece(hor, ver, pieceType, pieceColor)

    # kijken als de koning in gevaar komt door de zet
    if isKingInDanger(PieceCodeToColor(pieceColor)):
        # Indien ja, herstel het bord
        Board.chess_board = Board.chess_board_BAK
        print(Fore.RED + "Je brengt je koning in gevaar!" + Fore.RESET)
        return False
    
    return True