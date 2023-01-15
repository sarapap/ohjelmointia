"""
Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
"""
luku_1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku_2 = int(input("Anna toinen kokonaisuku: "))
luku_3 = int(input("Anna kolmas kokonaisluku: "))
summa = luku_1 + luku_2 + luku_3
print(f"Kokonaislukujen summa on {summa}.")
tulo = luku_1 * luku_2 * luku_3
print(f"Kokonaislukujen tulo on {tulo}.")
keskiarvo = (luku_1 + luku_2 + luku_3)/(3)
print(f"Kokonaislukujen keskiarvo on {keskiarvo}.")

