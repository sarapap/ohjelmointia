"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
"""

luvut = []
jakaja = 1
kokonaisluku = int(input("Anna kokonaisluku: "))

while jakaja <= kokonaisluku:
    if kokonaisluku % jakaja == 0:
        luvut.append(jakaja)
    jakaja = jakaja + 1

if luvut[0] == 1 and luvut[1] == kokonaisluku:
    print("Luku on alkuluku.")
else:
    print("Luku on kokonaisluku.")


