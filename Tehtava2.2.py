import math

radius_str = input("Lasken sinulle ympyrän pinta-alan. Anna ympyrän säde: ")
radius = float(radius_str)
pinta_ala = radius**2*math.pi

print(f"Tämän ympyrän pinta-ala on {pinta_ala:.2f}.")