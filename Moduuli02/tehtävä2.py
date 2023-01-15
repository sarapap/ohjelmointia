""""
Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
"""
import math

# pi * r^2
r = float(input("Anna ympyrän säde: "))
area = math.pi * r * r
print(f"Ympyrän pinta-ala on {area} neliömetriä.")
