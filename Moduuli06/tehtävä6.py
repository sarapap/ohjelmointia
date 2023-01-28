"""
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan
halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
"""
# ympyrän pinta-ala pii * r * r = pii * halkaisija
# kerrotaan sadalla, jotta saadaan neliömetrit senttimetreistä
import math
def pizza(halkaisija, hinta):
    yksikköhinta = hinta // math.pi * halkaisija * 100
    return yksikköhinta

pizza_1h = float(input("Anna 1. pizzan halkaisija: "))
pizza_1e = float(input("Anna 1. pizzan hinta: "))
tulos_1 = pizza(pizza_1h, pizza_1e)
pizza_2h = float(input("Anna 2. pizzan halkaisija: "))
pizza_2e = float(input("Anna 2. pizzan hinta: "))
tulos_2 = pizza(pizza_2h, pizza_2e)
if tulos_1 > tulos_2:
    print("2. pizza on parempi vastine rahoille.")
else:
    print("1. pizza on parempi vastine rahoille.")


