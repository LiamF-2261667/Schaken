from Piece import GetPieceType, GetPieceColor


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

hor = 1
ver = 1

# Het selecteren van een stuk (bv: A6)
def selectInput():
    # Aanvragen van de input en omzetten naar een array
    selected = list(input("Geef het coordinaat van het stuk dat u wilt selecteren: "))

    # Letter in een hoofdletter zetten
    letter = str.capitalize(selected[0])
    # Testen of de eerste invoer daadwerkelijk een letter is
    if str.isalpha(letter) == False:
        print("Foutieve invoer, de eerst moet de letter gegeven worden!")
        return

    # Testen als de tweede invoer daadwerkelijk een cijfer is en omzetten van een string naar een integer
    try: 
      number = int(selected[1])
    except ValueError:
      print("Foutieve invoer, als tweede moet het cijfer gegeven worden!")
      return
    
    # Selectie opslaan
    hor = letterToNumber(letter)
    ver = number

    # Testen als de invoer een coordinaat kan zijn
    if hor == "null":
        print("Deze letter behoord niet tot het schaakbord!")
        return
    
    if ver > 8:
        print("Dit nummer behoord niet tot het schaakbord!")
        return
    
    if ver < 1:
        print("Dit nummer behoord niet tot het schaakbord!")
        return

    # Testen als er een stuk daadwerkelijk is op deze positie
    if GetPieceType(hor, ver) == "null":
        print("Er staat geen stuk op deze positie")
        return
    
    if GetPieceType(hor, ver) == "404":
        print("ERROR: 404")
    
    # Tijdelijke output
    print("Er staat een " + GetPieceColor(hor, ver) + " " + GetPieceType(hor, ver) + " op het coordinaat " + selected[0] + selected[1])
