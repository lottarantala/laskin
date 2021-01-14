def yhteenlasku():
    try:
        luku1 = float(input("Anna luku 1: "))
        luku2 = float(input("Anna luku 2: "))
        summa = luku1 + luku2
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        print("Lukujen {} ja {} summa on {}".format(luku1, luku2, summa))

def vahennyslasku():
    try:
        luku1 = float(input("Anna luku 1: "))
        luku2 = float(input("Anna luku 2: "))
        erotus = luku1 - luku2
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        print("Lukujen {} ja {} erotus on {}".format(luku1, luku2, erotus))

def kertolasku():
    try:
        luku1 = float(input("Anna luku 1: "))
        luku2 = float(input("Anna luku 2: "))
        tulo = luku1 * luku2
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        print("Lukujen {} ja {} tulo on {}".format(luku1, luku2, tulo))

def potenssi():
    try:
        luku1 = float(input("Anna luku 1: "))
        luku2 = float(input("Anna luku 2: "))
        potenssi = luku1 ** luku2
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        print("Luku {} potenssiin {} on {}".format(luku1, luku2, potenssi))

def jakolasku():
    try:
        luku1 = float(input("Anna luku 1: "))
        luku2 = float(input("Anna luku 2: "))
        osamaara = luku1 / luku2
    except ZeroDivisionError:
        print("Tällä ohjelmalla ei pääse äärettömyyteen")
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        print("Lukujen {} ja {} osamäärä on {}".format(luku1, luku2, osamaara))

while True:
    print("Operaatiot: +, -, *, /, ^ tai p(poistu)")
    operaatio = input("Valitse operaatio: ")    
    if operaatio == "+":
        yhteenlasku()
    elif operaatio == "-":
        vahennyslasku()
    elif operaatio == "*":
        kertolasku()
    elif operaatio == "/":
        jakolasku()
    elif operaatio == "^":
        potenssi()
    elif operaatio == "p":
        break
    elif operaatio == "P":
        break
    else:
        print("Operaatiota ei ole olemassa")