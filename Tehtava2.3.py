print("Lasketaan suorakulmion piiri ja pinta-ala.")

kanta_str = input("Anna ensin suorakulmion kannan pituus senttimetreinä: ")
kanta = float(kanta_str)
korkeus_str = input("Anna vielä suorakulmion korkeus senttimetreinä: ")
korkeus = float(korkeus_str)

piiri = 2*kanta+2*korkeus
pinta_ala = kanta*korkeus

print(f"Tämän suorakulmion piirin pituus on {piiri:4.2f} senttimetriä.")
print(f"Tämän suorakulmion pinta-ala on {pinta_ala:4.2f} neliösenttimetriä.")