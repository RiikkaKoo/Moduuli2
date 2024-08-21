print("Lasketaan suorakulmion piiri ja pinta-ala.")

kanta_str = input("Anna ensin suorakulmion kannan pituus: ")
kanta = float(kanta_str)
korkeus_str = input("Anna vielä suorakulmion korkeus: ")
korkeus = float(korkeus_str)

piiri = 2*kanta+2*korkeus
pinta_ala = kanta*korkeus

print(f"Tämän suorakulmion piirin pituus on {piiri:.2f}.")
print(f"Tämän suorakulmion pinta-ala on {pinta_ala:.2f}.")