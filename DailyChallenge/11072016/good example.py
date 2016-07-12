def checkSymbol(element, symbol):
    element = element.lower()
    symbol = symbol.lower()
    length = len(element)    

    if len(symbol) != 2: return False
    if symbol[0] not in element: return False
    if symbol[1] not in element: return False

    for i in range(0, length):
        if symbol[0] == element[i]:
            for j in range(i + 1, length):
                if symbol[1] == element[j]: return True
    return False

# Bonus 1 and 2
def listSymbols(element):
    element = element.lower()
    allSymbols = []
    for i in range(0, len(element)):
        for j in range(i + 1, len(element)):
            newSymbol = ''.join((element[i].upper(), element[j]))
            if newSymbol not in allSymbols: allSymbols.append(newSymbol)
    allSymbols = sorted(allSymbols)
    return allSymbols

 def firstSymbol(element):
     allSymbols = listSymbols(element)
    return allSymbols[0]

def countSymbols(element):
    allSymbols = listSymbols(element)
    return len(allSymbols)

print checkSymbol("Spenglerium", "Ee")
print checkSymbol("Zeddemorium", "Zr")
print checkSymbol("Venkmine", "Kn")
print checkSymbol("Stantzon", "Zt")
print checkSymbol("Melintzum", "Nn")
print checkSymbol("Tullium", "Ty")

print firstSymbol("Gozerium")
print firstSymbol("Slimyrine")

print countSymbols("Zuulon")