"""
Kirjoita ohjelma,
joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
"""

tuuma = float(input("Anna tuuma: "))
while tuuma >= 0:
    if tuuma <= 0:
        break
    cm = tuuma * 2.54
    print(cm)
    tuuma = float(input("Anna tuuma: "))
print("Toiminnot lopetettu.")

