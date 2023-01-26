"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.
"""
import random
silmäluvut = []
summa = 0
kerrat = 0

kuutiot = int(input("Anna arpakuutioiden lukumäärä: "))
while kerrat < kuutiot:
    silmäluku = random.randint(1,6)
    silmäluvut.append(silmäluku)
    kerrat = kerrat + 1
for silmäluku in silmäluvut:
    summa = summa + silmäluku
print(f"Silmälukujen summa on {summa}")