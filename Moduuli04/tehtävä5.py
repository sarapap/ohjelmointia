"""
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
(Oikea käyttäjätunnus on python ja salasana rules).
"""
oikea_1 = "python"
oikea_2 = "rules"
kerrat = 0
while True:
    tunnus = str(input("Käyttäjätunnus: "))
    salasana = str(input("Salasana: "))
    if tunnus == oikea_1 and salasana == oikea_2:
        print("Tervetuloa.")
        break
    kerrat = kerrat + 1
    if kerrat == 5:
        print("Pääsy evätty.")
