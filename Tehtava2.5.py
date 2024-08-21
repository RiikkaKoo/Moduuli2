GRAMMA = 1
LEVISKA = 20*(32*13.3)
NAULA = 32*13.3
LUOTI = 13.3*GRAMMA

leviskat = float(input("Anna leviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammoina = float(leviskat*LEVISKA+naulat*NAULA+luodit*LUOTI)
kilot = float((grammoina-(grammoina % 1000))/1000)

print(f"Massa nykymittojen mukaan:\n{kilot:.0f} kilogrammaa ja {grammoina % 1000:.0f} grammaa.")