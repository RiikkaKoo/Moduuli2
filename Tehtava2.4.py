print("Lasketaan kolmen luvun summa, tulo ja keskiarvo.")

eka_str = input("Anna ensimmäinen luku: ")
toka_str = input("Anna toinen luku: ")
kolmas_str = input("Anna kolmas luku: ")
eka = float(eka_str)
toka = float(toka_str)
kolmas = float(kolmas_str)

summa = eka+toka+kolmas
tulo = eka*toka*kolmas
keskiarvo = summa/3

print(f"Näiden lukujen summa on {summa:4.2f}.")
print(f"Näiden lukujen tulo on {tulo:4.2f}.")
print(f"Näiden lukujen keskiarvo on {keskiarvo:4.2f}.")