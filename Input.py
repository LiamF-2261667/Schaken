import os

from Piece import GetPieceType, GetPieceColor, SetPiece, PieceNameToLetter, PieceColorToCode, RemovePiece
from Board import DrawBoard


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

    if len(dest) < 2:
        print("Foutieve invoer, geef eerst de letter en daarna het cijfer in!")
        return "null"

    # Letter in een hoofdletter zetten
    letter = str.capitalize(dest[0])
    # Testen of de eerste invoer daadwerkelijk een letter is
    if str.isalpha(letter) == False:
        print("Foutieve invoer, de eerst moet de letter gegeven worden!")
        return "null"

    # Testen als de tweede invoer daadwerkelijk een cijfer is en omzetten van een string naar een integer
    try: 
      number = int(dest[1])
    except ValueError:
      print("Foutieve invoer, als tweede moet het cijfer gegeven worden!")
      return "null"
    
    # Selectie opslaan
    hor = letterToNumber(letter)
    ver = number

    # Testen als de invoer een coordinaat kan zijn
    if hor == "null":
        print("Deze letter behoord niet tot het schaakbord!")
        return "null"
    
    if ver > 8:
        print("Dit nummer behoord niet tot het schaakbord!")
        return "null"
    
    if ver < 1:
        print("Dit nummer behoord niet tot het schaakbord!")
        return "null"
    
    # destination returnen
    return hor, ver, letter

selectedHor = 1
selectedVer = 1

# Het selecteren van een stuk (bv: A6)
def selectInput():
    selected = coordToNumbersArray("Geef het coordinaat van het stuk dat u wilt selecteren: ")

    # Testen als de invoer correct was
    if selected == "null":
        return False

    hor = selected[0]
    ver = selected[1]
    letter = selected[2]

    # Testen als er een stuk daadwerkelijk is op deze positie
    if GetPieceType(hor, ver) == "null":
        print("Er staat geen stuk op deze positie")
        return False
    
    if GetPieceType(hor, ver) == "404":
        print("ERROR: 404")
        return False
    
    # De selectie globaal maken
    global selectedHor
    selectedHor = hor

    global selectedVer
    selectedVer = ver

    # Output
    print("Er staat een " + GetPieceColor(hor, ver) + " " + GetPieceType(hor, ver) + " op het coordinaat " + letter + str(ver))
    
    return True


def destinationInput():
    dest = coordToNumbersArray("Geef het coordinaat van de gewenste verplaatsing: ")

    # Testen als de invoer correct was
    if dest == "null":
        return
    
    hor = dest[0]
    ver = dest[1]

    # Informatie voor het nieuwe stuk verzamelen
    pieceTypeStr = GetPieceType(selectedHor, selectedVer)
    pieceType = PieceNameToLetter(pieceTypeStr)
    
    pieceColorStr = GetPieceColor(selectedHor, selectedVer)
    pieceColor = PieceColorToCode(pieceColorStr)

    # Het oude stuk verwijderen en het nieuwe stuk plaatsen
    RemovePiece(selectedHor, selectedVer)

    SetPiece(hor, ver, pieceType, pieceColor)

    # Clear de console
    os.system("clear")

    # Tekenen het bord met de aanpassing
    DrawBoard()